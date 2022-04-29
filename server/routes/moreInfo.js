const express = require("express");
const router = express.Router();
const {
  postInfo,
  patchById,
  getById,
  getInfo,
  getLabs,
  getDepartment,
  getCollege,
  getExplist,
  getLabsfromdepartment,
  getSelectedExplist
  
} = require("../controllers/moreInfoController");

router.post("/", postInfo);

router.patch("/edit", patchById);

router.get("/:_id", getById);

router.get("/", getInfo);

router.get("/all/college", getCollege);

router.post("/department", getDepartment);

router.post("/labs", getLabs);

router.post("/experiment",getExplist)

router.post("/labs/depandclg",getLabsfromdepartment)

router.post("/selected",getSelectedExplist)
 

module.exports = router;
