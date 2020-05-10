python -c 'import crypt; print crypt.crypt("user_password", "$5$sha-256")'

python -c 'import crypt; print crypt.crypt("user_password", "$5$sha-512")'

python -c 'import crypt; print crypt.crypt("user_password", "$5$MD5")'
