const express = require("express");
const router = express.Router();

const {
  getAll,
  getById,
  postNote,
  patchNotes,
  deleteNotes,
} = require("../controllers/noteController");

// @route GET /posts
// @desc a get req for posts routes
// @access public
router.get("/", getAll);

router.get("/:runID", getById);

router.post("/", postNote);

router.patch("/:runID", patchNotes);

router.delete("/:runID", deleteNotes);

module.exports = router;
