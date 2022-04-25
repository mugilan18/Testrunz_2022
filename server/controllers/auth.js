const User = require("../models/Users");
const Experiment = require("../models/Experiments");
const jwt = require("jsonwebtoken");
const _ = require("lodash");
const expressJWT = require("express-jwt");
const { OAuth2Client } = require("google-auth-library");
const fetch = require("node-fetch");
const nodemailer = require('nodemailer')
require("dotenv").config();


const expiretime = 60*60*24*5
const creatToken=(id)=>{
  return jwt.sign({id},"testrunsecrettoken",{
    expiresIn:expiretime
  })
}




const authAccountregister = (req, res) => {
  //const { token } = req.body;
  console.log(req.body)
    
    User.create({
        email : req.body.email,
        name : req.body.name,
        role : req.body.role || "student",
        labtype:req.body.labtype||[],
        department:req.body.department||"",
        collegeName:req.body.collegeName||""
      }).then((user)=>{
        console.log(user.json())
       return res.json({status:"ok"})
      })
    .catch((err)=>{
    return  res.json({status:err})
    })
      
   
  
};

const authAccountlogin = (req, res, next) => {
  const email  = req.body.email;
  User.findOne({ email })
    .exec()
    .then((user) => {
      const jwttoken = creatToken(user._id) ;
              console.log("here is the token",jwttoken);
              res.json({
                jwttoken,
              });
    })
    .catch((error) => {
      return res.status(400).json({ error: "User with that email not exits" });
    });
};

const adminMiddleware = (req, res, next) => {
  User.findById(req.user._id)
    .exec()
    .then((user) => {
      if (!user)
        return res
          .status(400)
          .json({ error: "User with this email does'nt exits" });
      if (user.role !== "admin") {
        return res.status(400).json({ error: "Admin resource access denied" });
      }
      req.profile = user;
      next();
    })
    .catch((error) => {
      return res.status(400).json({ error });
    });
};





      
const googleLogin = (req, res, next) => {
  const email  = req.body.email;
        User.findOne({ email })
          .exec()
          .then((user) => {

            if (!user) {
              User.create({
                email : req.body.email,
                name : req.body.name
              }).then((user)=>{
                const { _id, email,name, role} = user;
                console.log(_id,email,name)
                res.json({
                  user: { _id, email, name, role },
                });
              })
            }
          else {
              const { _id, email, name, role } = user;
              const jwttoken = creatToken(user._id) ;
              console.log("here is the token",jwttoken);
              res.json({
                jwttoken,
              });
            }
          })
        
};

const deleteuser=(req, res, next)=>{
  const userid  = req.body.userid;
  console.log(userid)
  Experiment.deleteMany({userid:userid})
  .then(()=>{
    console.log("experiments Deleted")
    User.deleteMany({_id:userid})
    .then((user)=>{
      console.log("user deleted")
      res.json({
        detail: "user Deleted",
      });
      });
    });
}


//jwt validation added at march
const validateuser=(req, res, next)=>{
  const usertoken  = req.body.usertoken;
  // console.log(req.body)
jwt.verify(usertoken,"testrunsecrettoken",(err,decoded)=>{
if(err){
  // res.json({"error":"error"})
  console.log(err)
  
}
else{
  console.log(decoded)
  User.findById({ _id:decoded.id })
  .exec()
  .then((user) => {

    if (!user) {
     res.json({"err":"no such user"})
     console.log("no such user")
    }
  else {
      const { _id, email, name, role ,showOnce,collegeName,state,country,department,semester,year,labtype} = user;
      console.log(user)
      res.json({
        user: { _id, email, name, role,showOnce,collegeName,state,country,department,semester,year,labtype},
      });
    }
  })


}
})
}





const ceratemailUser = async (req, res) => {
  console.log("mail content",req.body)
  
  
  let message =`The account in testrunz is created for ${req.body.name}  with the mail id of ${req.body.email} and the password is  ${req.body.password}  , You can change the password in forgot password tab to create your own password.` 
  
  var transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: process.env.EMAIL,
      pass: process.env.EMAILPASS
    }
  });
  
   
  var mailOptions = {
    from: process.env.EMAIL,
    to: req.body.email,
    subject: 'Account created in  Testrunz',
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


  const showallUser = (req, res, next) => {
    User.find({}, function(err, result) {
      if (err) {
        console.log(err);
      } else {
        res.json(result);
      }
    });
  };

module.exports = {
  authAccountregister,
  authAccountlogin,
  adminMiddleware,
  googleLogin,
  deleteuser,
  validateuser,
  ceratemailUser,
  showallUser
};
