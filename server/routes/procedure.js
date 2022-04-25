const express = require("express");

const router = express.Router();

const {
  getProcedures,
  getProcedureById,
  searchTitle,
  testId,
  postProcedure,
  patchProcedure,
  deleteProcedure,
} = require("../controllers/procedureController");

router.get("/", getProcedures);

router.get("/:_id", getProcedureById);

router.get("/search/:title", searchTitle);

router.get("/test/:_id", testId);

router.post("/", postProcedure);

router.patch("/edit", patchProcedure);

router.delete("/:_id", deleteProcedure);

module.exports = router;
