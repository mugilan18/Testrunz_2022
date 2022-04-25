const router = require("express").Router();
const usersController = require("../controllers/users");
const authController = require("../controllers/auth");
const labController = require("../controllers/users");
const usermanage = require("../controllers/users");
const labControlleradmin = require("../controllers/users")
router.get("/users/:id",  usersController.read);
router.patch(
  "/users/update",
  usersController.update
);
router.patch(
  "/admin/update",

  authController.adminMiddleware,
  usersController.update
);
router.patch("/tooglelab",labController.patchlab)
router.patch("/tooglelab/admin",labControlleradmin.patchlabadmin)

router.post(
  "/getaccess",usermanage.getaccess);


module.exports = router;
