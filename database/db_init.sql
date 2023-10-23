CREATE TABLE "ElementsToProcess" (
    "id" serial PRIMARY KEY,
    "idBulk" integer NOT NULL,
    "retries" integer,
    "status" integer NOT NULL,
    "name" character varying(100) NOT NULL
);

CREATE INDEX "ElementsToProcess_idBulk_IDX" ON "ElementsToProcess" USING btree ("idBulk", "status");
CREATE INDEX "ElementsToProcess_status_IDX" ON "ElementsToProcess" USING btree ("status");

INSERT INTO "ElementsToProcess" ("idBulk", "retries", "status", "name")
VALUES
    (1, 0, 20, 'Element 1'),
    (1, 1, 20, 'Element 2'),
    (2, 2, 20, 'Element 3'),
    (2, 0, 20, 'Element 4'),
    (3, 0, 60, 'Element 5'),
    (3, 1, 60, 'Element 6'),
    (4, 2, 60, 'Element 7'),
    (5, 0, 80, 'Element 8'),
    (5, 1, 80, 'Element 9'),
    (6, 0, 100, 'Element 10');
