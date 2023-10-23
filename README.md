sudo -u postgres psql

DROP DATABASE masleads;
DROP ROLE masleads;

CREATE ROLE masleads WITH PASSWORD 'masleads-pwd';
ALTER ROLE masleads WITH LOGIN;
CREATE DATABASE masleads WITH OWNER masleads;
\c masleads
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE "ElementsToProcess" TO masleads;
GRANT USAGE ON SCHEMA public TO masleads;
GRANT USAGE, SELECT ON SEQUENCE "ElementsToProcess_id_seq" TO masleads;
