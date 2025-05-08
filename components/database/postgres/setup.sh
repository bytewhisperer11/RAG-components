#!/bin/bash
set -euo pipefail
trap 'echo -e "\033[1;31m[ERROR]\033[0m Line $LINENO: Command failed: $BASH_COMMAND"' ERR

# ----------------------------------
# Configurable Variables
# ----------------------------------
PG_USER="postgres"
DB_NAME="vector_db"
PGVECTOR_REPO="https://github.com/pgvector/pgvector.git"
PGVECTOR_TEST_DIM=3

# ----------------------------------
# Logging Utilities
# ----------------------------------
info() { echo -e "\033[1;34m[INFO]\033[0m $1"; }
success() { echo -e "\033[1;32m[SUCCESS]\033[0m $1"; }
fail() { echo -e "\033[1;31m[FAIL]\033[0m $1"; }

# ----------------------------------
# Step 1: Install PostgreSQL
# ----------------------------------
if command -v psql >/dev/null; then
    info "PostgreSQL already installed."
else
    info "Installing PostgreSQL..."
    sudo apt update
    sudo apt install -y postgresql postgresql-contrib
    success "PostgreSQL installed."
fi

# ----------------------------------
# Step 2: Start and Enable PostgreSQL
# ----------------------------------
info "Ensuring PostgreSQL service is active..."
sudo systemctl enable postgresql
sudo systemctl start postgresql
success "PostgreSQL service running."

# ----------------------------------
# Step 3: Install pgvector Extension
# ----------------------------------
VECTOR_CONTROL_PATH="$(pg_config --sharedir)/extension/vector.control"
if [ -f "$VECTOR_CONTROL_PATH" ]; then
    info "pgvector extension already installed."
else
    info "Cloning and installing pgvector..."
    git clone "$PGVECTOR_REPO"
    cd pgvector
    make
    sudo make install
    cd ..
    rm -rf pgvector
    success "pgvector extension installed."
fi

# ----------------------------------
# Step 4: Create Database if Needed
# ----------------------------------
info "Checking if database '$DB_NAME' exists..."
if ! sudo -u "$PG_USER" psql -tAc "SELECT 1 FROM pg_database WHERE datname = '$DB_NAME'" | grep -qw 1; then
    sudo -u "$PG_USER" psql -c "CREATE DATABASE $DB_NAME;"
    success "Database '$DB_NAME' created."
else
    info "Database '$DB_NAME' already exists."
fi

# ----------------------------------
# Step 5: Enable pgvector in Database
# ----------------------------------
info "Enabling pgvector in '$DB_NAME'..."
sudo -u "$PG_USER" psql -d "$DB_NAME" -c "CREATE EXTENSION IF NOT EXISTS vector;"
success "pgvector extension enabled for '$DB_NAME'."

# ----------------------------------
# Step 6: Verification – Create and Use Test Table
# ----------------------------------
info "Running end-to-end test using a dummy vector table..."
sudo -u "$PG_USER" psql -d "$DB_NAME" -c "
CREATE TABLE IF NOT EXISTS test_vectors (
    id SERIAL PRIMARY KEY,
    embedding vector($PGVECTOR_TEST_DIM)
);
INSERT INTO test_vectors (embedding) VALUES ('[1,2,3]');
SELECT * FROM test_vectors;
"
success "Vector data inserted and retrieved successfully."

# ----------------------------------
# Final Verification
# ----------------------------------
info "Verifying extension registration..."
EXT_INSTALLED=$(sudo -u "$PG_USER" psql -d "$DB_NAME" -tAc "SELECT extname FROM pg_extension WHERE extname = 'vector'")
if [[ "$EXT_INSTALLED" == "vector" ]]; then
    success "pgvector extension is active in '$DB_NAME'."
else
    fail "pgvector extension not found in database!"
    exit 1
fi

success "PostgreSQL + pgvector setup complete and verified."
