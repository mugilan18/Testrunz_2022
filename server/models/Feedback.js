const mongoose = require("mongoose");
const Schema = mongoose.Schema;
// create Schema
const feedbackSchema = new Schema({
  
    postedby: {
    type: String,
    required: true,
  },
//  rating: {
//     type: Number,
//     required: true,
//   },
  feedback: {
    type: String,
    required: true,
  },
  status: {
    type: String,
    default:"opened"
  },
  type: {
    type: String,
  },
  time: {
    type: Number,
    default: new Date().getTime(),
  },
  assignedto:{
    type:String,
  },
  image:{
    type:String,
  }


});

module.exports = Feedback = mongoose.model("feedback", feedbackSchema);
