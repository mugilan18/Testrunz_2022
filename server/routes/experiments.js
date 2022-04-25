const express = require("express");
const router = express.Router();

const {
  getExpAllUser,
  getSingleUser,
  postUser,
  patchUser,
  patchUser1,
  deleteUser,
  mailUser,
  removesharedUser,
  getExpAllUsermail
  
} = require("../controllers/experimentController");

// @route GET all /users
// @desc a get req for users routes
// @access public
router.get("/runz/:_id", getExpAllUser);
router.post("/mypage", getExpAllUsermail);
// @route GET single /users/<>
// @desc a get req for users routes
// @access public
router.get("/:_id", getSingleUser);

// @route POST /users/create
// @desc a POST req for users registeration
// @access public
router.post("/", postUser);

router.post("/mail", mailUser);

// @route PATCH /users/update/<>
// @desc a PATCH req for users registeration
// @access public
router.patch("/:_id", patchUser);
router.patch("/remove/:_id",removesharedUser);

router.patch("/", patchUser1);

// @route Delete /users/delete
// @desc a PATCH req for users registeration
// @access public
router.delete("/:_id", deleteUser);
module.exports = router;
