const { v4: uuidv4 } = require("uuid");
const nodemailer = require('nodemailer')
// load user model
const User = require("../models/Experiments");

const Usernames = require("../models/Users")

// load validator
const validateRegisterInput = require("../validation/register");

const getExpAllUser = async function (req, res, next) {
  console.log("user id cj=jandjad",req.params._id);
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
    res.json({ data: users.reverse(), totalCount: users.length });
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

const postUser =async (req, res, next) => {
  console.log(req.body)
  const { errors, isValid } = validateRegisterInput(req.body);

  // check validation
  if (!isValid) {
    return res.status(400).json(errors);
  }
  try {
    const user = await User.findOne({ $and: [  {userid: req.body.userId },  {experimentName: req.body.experimentName} ] } );
    if (user) {
      return res.json({"errors":"already created"});
    }
    else{
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
    }
  } catch (err) {
    console.error(err);
    res.json(err);
  }
  

};






//post bulk user 
const   postBulkuser =async (req, res, next) => {
  console.log(req.body)
      let email = req.body.email
      let procedureDescription = req.body.procedureDescription
      let labType = req.body.labType
      let experimentName =  req.body.experimentName
      let assignedby = req.body.assignedby
      let count= req.body.email.length
      let noname =[]
      let validname =[]
  try {
    for (let i = 0; i < count; i++) {
      console.log("individual",email[i])
      const user = await Usernames .findOne({email:email[i]})
      if(user){
        const newUser = new User({
            runID: uuidv4(),
            studentName: user.name,
            procedureDescription: procedureDescription,
            labType:labType,
            experimentName:experimentName,
            userid: user._id,
            status:"assigned",
            assignedBy:assignedby
          });
          newUser
            .save()
            .then((user) => console.log("individual",newUser))
            .catch((err) => console.error(err));
            validname.push(email[i])
      }
      else{
        noname.push(email[i])
      }
     
    }
    res.json({"sent":validname})
    console.log("sent",validname)
    console.log("unsent",noname)
  }
  // const { errors, isValid } = validateRegisterInput(req.body);

  // // check validation
  // if (!isValid) {
  //   return res.status(400).json(errors);
  // }
  // try {
  //   const user = await User.findOne({ $and: [  {userid: req.body.userId },  {experimentName: req.body.experimentName} ] } );
  //   if (user) {
  //     return res.json({"errors":"already created"});
  //   }
  //   else{
  // //User.findOne()
  // const newUser = new User({
  //   runID: uuidv4(),
  //   studentName: req.body.studentName,
  //   procedureDescription: req.body.procedureDescription,
  //   labType: req.body.labType,
  //   experimentName: req.body.experimentName,
  //   userid: req.body.userId
  // });
  // newUser
  //   .save()
  //   .then((user) => res.json(user))
  //   .catch((err) => console.error(err));
  //   }
  // } 
  catch (err) {
    console.error(err);
    res.json(err);
  }
  

};



// group mypage with department
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



// $pull: { fruits: { $in: [ "apples", "oranges" ] }, vegetables: "carrots"
const getExpBymail = async (req, res) => {
  console.log("PATCH", req.body)
  try {
    const metas = await User.find({ $and: [ {shareWith: {$in: [req.body.email]}}, {assignedBy:req.body.email }  ] } )
    // const metas = await User.aggregate( [
    //     {$match:{ $and: [{ shareWith: req.body.email},{ assignedBy : { $ne: req.body.email
    //   } } ] }
         
    //   } 
    // ] );
    // const ids = metas.map((obj) => obj);
    // res.json({ ids});
    // console.log( ids)

  //   const metas = await User.aggregate( [
  //     {$match:{ shareWith: req.body.email }}, 
  //     {$group: { _id: "$labType" }}
    
  // ] );
  const metasother = await User.find({ $and: [{ shareWith: req.body.email},{ assignedBy : { $ne: req.body.email } } ] })
  res.json({ metas,metasother});
  // console.log( ids)
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

const postspecificexp = async (req, res) => {
  console.log(req.body)
  let lab=req.body.lab
  let email =req.body.email
  let experiment =req.body.experiment
  let college =req.body.college
  try {
    const metas= await User.find({ $and: [{ shareWith:email},{ assignedBy:email},{experimentName:experiment} ] })
    res.json({metas})
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
  getExpAllUsermail,
  postBulkuser,
  getExpBymail,
  postspecificexp

};
