const { v4: uuidv4 } = require("uuid");
const nodemailer = require('nodemailer')
// load user model
const User = require("../models/Experiments");

// load validator
const validateRegisterInput = require("../validation/register");

const getExpAllUser = async function (req, res, next) {
  // console.log("user id",req.params._id);
  try {
    const users = await User.find({userid: req.params._id});
    /* 
      // filter in server
      const newUsers = users.map(
        ({ runID, studentName, labType, experimentName }) => ({
          runID,
          studentName,
          labType,
          experimentName,
        })
      ); */
    console.log("output",users.length);
    res.json({ data: users, totalCount: users.length });
  } catch (err) {
    console.error(err);
  }
};

const getExpAllUsermail = async function (req, res, next) {
  console.log("usersgjgsid", JSON.stringify(req.body._id));
  try {
    const users = await User.find({shareWith: req.body._id});
    /* 
      // filter in server
      const newUsers = users.map(
        ({ runID, studentName, labType, experimentName }) => ({
          runID,
          studentName,
          labType,
          experimentName,
        })
      ); */
    console.log("output",users.length);
    res.json({ data: users, totalCount: users.length });
  } catch (err) {
    console.error(err);
  }
};


const getSingleUser = async function (req, res, next) {
  try {
    const user = await User.findOne({ _id: req.params._id });
     console.log("hellooo",user)
    console.log("hello",req.params._id)
     res.json(user);
  } catch (err) {
    console.error(err);
    res.json(err);
  }
};

const postUser = (req, res, next) => {
  console.log(req.body)
  const { errors, isValid } = validateRegisterInput(req.body);

  // check validation
  if (!isValid) {
    return res.status(400).json(errors);
  }

  //User.findOne()
  const newUser = new User({
    runID: uuidv4(),
    studentName: req.body.studentName,
    procedureDescription: req.body.procedureDescription,
    labType: req.body.labType,
    experimentName: req.body.experimentName,
    userid: req.body.userId
  });
  newUser
    .save()
    .then((user) => res.json(user))
    .catch((err) => console.error(err));
};
// $pull: { fruits: { $in: [ "apples", "oranges" ] }, vegetables: "carrots"
const patchUser = async (req, res) => {
  console.log("PATCH", req.body)
  try {
    const updatedUser = await User.findByIdAndUpdate(
      { _id: req.params._id },
      {
         $addToSet: {
          shareWith: req.body.sharewith} ,
        $set: {
          procedureDescription: req.body.procedureDescription,
          labType: req.body.labType,
          experimentName: req.body.experimentName,
          sharedDate:new Date().getTime(),
        },
      }
    );
    res.json(updatedUser); 
  } catch (err) {
    console.error(err);
  }
};


// Remove Shared user 
const removesharedUser = async (req, res) => {
  console.log("remove shared", req.body)
  try {
    const updatedUser = await User.findByIdAndUpdate(
      { _id: req.params._id },
      {
        $pull: { shareWith: req.body.email}
      }
    );
    res.json(updatedUser); 
  } catch (err) {
    console.error(err);
  }
};

// add data to experiments
const patchUser1 = async (req, res) => {
  const {id, ...other} = req.body;
  console.log("PATCH", other)
   try {
    const updatedUser = await User.findByIdAndUpdate(
      { _id: id },
      {
        $set: {
          datas: other,
          
        },
      }
    );
    res.json(updatedUser);
  } catch (err) {
    console.error(err);
  } 

};


const deleteUser = async (req, res) => {
  try {
    const removedUser = await User.remove({ _id: req.params._id });
    res.json(removedUser);
  } catch (err) {
    console.error(err);
  }
};


const mailUser = async (req, res) => {
console.log("mail content",req.body)


let message =`${req.body.name} submitted the prodedure of ${req.body.experimentName} from ${req.body.labType} Lab open the following Link to check${ process.env.MAIL_URL+req.body._id}` 

var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: process.env.EMAIL,
    pass: process.env.EMAILPASS
  }
});


var mailOptions = {
  from: process.env.EMAIL,
  to: req.body.sharewith,
  subject: 'Sharing Runz',
  text: message 
};



transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log("here comes the error",error);
    res.json("error")
  } else {
    res.json("sent!!!")
    console.log('Email sent!!!');
  }
});



};

module.exports = {
  getExpAllUser,
  getSingleUser,
  postUser,
  patchUser,
  patchUser1,
  deleteUser,
  mailUser,
  removesharedUser,
  getExpAllUsermail
};
