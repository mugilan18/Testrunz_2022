const express = require("express");
const router = express.Router();

const {
  getAll,
  postFeedback,
  
} = require("../controllers/feedbackController");


 router.get("/", getAll);

// router.get("/:runID", getById);

router.post("/", postFeedback);

// router.patch("/:runID", patchNotes);

// router.delete("/:runID", deleteNotes);

module.exports = router;