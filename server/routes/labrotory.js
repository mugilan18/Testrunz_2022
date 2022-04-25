const express = require("express");
const router = express.Router();

const { getLab, postLab } = require("../controllers/laboratoryController");
// @route GET /profiles
// @desc a get req for profiles routes
// @access public
router.get("/", getLab);

router.post("/", postLab);

module.exports = router;
