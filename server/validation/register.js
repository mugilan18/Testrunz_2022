const validator = require("validator");
const isEmpty = require("./is_empty");

module.exports = function validateRegisterInput(data) {
  let errors = {};

  data.studentName = !isEmpty(data.studentName) ? data.studentName : "";
  data.labType = !isEmpty(data.labType) ? data.labType : "";
  data.experimentName = !isEmpty(data.experimentName)
    ? data.experimentName
    : "";

  if (!validator.isLength(data.studentName, { min: 2, max: 50 })) {
    errors.studentName = "Student name must be between 2 and 50 characters";
  }

  if (!validator.isLength(data.labType, { min: 2, max: 50 })) {
    errors.labType = "lab name must be between 2 and 50 characters";
  }

  if (!validator.isLength(data.experimentName, { min: 2, max: 50 })) {
    errors.experimentName =
      "Experiment name must be between 2 and 50 characters";
  }

  if (validator.isEmpty(data.studentName)) {
    errors.studentName = "Student Name Field Required";
  }
  if (validator.isEmpty(data.labType)) {
    errors.labType = "Lab Type Field Required";
  }
  if (validator.isEmpty(data.experimentName)) {
    data.experimentName = "Experiment Name Field Required";
  }

  return { errors, isValid: isEmpty(errors) };
};
