const router = require("express").Router();
const authController = require("../controllers/auth");

router.post( "/login", authController.authAccountlogin);
router.post("/register", authController.authAccountregister);

router.post("/google_login", authController.googleLogin);
router.delete("/deleteuser", authController.deleteuser);
router.post("/validateuser", authController.validateuser);
router.post("/usermail", authController.ceratemailUser);
router.get("/alluser", authController.showallUser);

module.exports = router;
