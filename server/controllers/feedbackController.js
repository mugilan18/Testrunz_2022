const Feedback = require("../models/Feedback");
const nodemailer = require('nodemailer')

const getAll = async function (req, res, next) {
  try {
    const feedbacks = await Feedback.find();
    res.json(feedbacks);
  } catch (err) {
    console.error(err);
  }

};

// const getById = async function (req, res, next) {
//   try {
//     const note = await Note.findOne({ runID: req.params.runID });
//     res.json(note);
//   } catch (err) {
//     console.error(err);
//   }
// };

const postFeedback = function (req, res, next) {
    console.log("triggered",req.body)
  const newFeedback = new Feedback({
    postedby: req.body.postedby,
    feedback: req.body.feedback,
    // rating: req.body.rating,
    image:req.body.image,
    type:req.body.type,
  });
  newFeedback
    .save()
    .then((result) => {
        console.log(result)
        res.json(result)




        let message =`${req.body.postedby} Send Feedback: ${req.body.feedback}  and a rating of ${req.body.rating}  stars` 

        var transporter = nodemailer.createTransport({
          service: 'gmail',
          auth: {
            user: process.env.EMAIL,
            pass: process.env.EMAILPASS
          }
        });
        
        
        var mailOptions = {
          from: process.env.EMAIL,
          to: process.env.EMAIL,
          subject: 'Feedback Recived',
          text: message,
        attachments: [
          // String attachment
          {
              filename: 'feedback.jpg',
              content: req.body.image.split("base64,")[1],
              encoding: "base64",


          },]
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
































    })
    .catch((err) => console.error(err));
};





module.exports = {postFeedback, getAll };
