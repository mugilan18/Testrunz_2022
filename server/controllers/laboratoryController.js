const Labrotory = require("../models/Labrotory");
const getLab = async function (req, res, next) {
  try {
    const labrotories = await Labrotory.find();

    res.json(labrotories);
  } catch (err) {
    console.error(err);
  }
};
const postLab = async function (req, res, next) {
  // console.error(req.body.exp);
  // res.json(req.body.exp)
  // lab=req.body.Lab
  // exp_oldName=req.body.exp_oldName
  // exp_newName=req.body.exp_newName
  // id=req.body.id
  // const labrotories = await Labrotory.findOne({_id:id});
  // index = labrotories.lab.indexOf(exp_oldName)
  // if (index !== -1) {
  // labrotories.lab[index]=exp_newName
  // }

  // Labrotory.updateMany({_id : id},{$pull:{lab:exp_oldName}})
  // if (lab in labrotories){
  //   index = labrotories.lab.indexOf(exp_oldName)
  //   console.log( "Has",lab)
  //   console.log( "index",index)
  // }
  // else{
  //   console.log("no")
  // }
//  console.log(labrotories)
//  console.log(labrotories.lab)


  // try {
  //   const labrotories = await Labrotory.find({});

  //   if (labrotories.length === 0) {
  //     const newEntry = new Labrotory({
  //       [req.body.name]: [req.body.experiment],
  //     });
  //     newEntry
  //       .save()
  //       .then((result) => res.json(result))
  //       .catch((err) => console.error(err));
  //   } else {
  //     for (const [key, value] of Object.entries(labrotories[0]["_doc"])) {
  //       if (key === req.body.name) {
  //         value.push(req.body.experiment);
  //         await Labrotory.findOneAndUpdate(
  //           { _id: labrotories[0]["_doc"]["_id"] },
  //           { [key]: value }
  //         );

  //         return res.json({ value: "new value updated" });
  //       } else {
  //         labrotories[0]["_doc"][req.body.name] = [req.body.experiment];
  //         await Labrotory.findOne(
  //           { _id: labrotories[0]["_doc"]["_id"] },
  //           function (err, result) {
  //             result[req.body.name] = [req.body.experiment];
  //             result.save();
  //           }
  //         );

  //         return res.json({ value: "new entry updated" });
  //       }
  //     }
  //     return res.json({ value: "Labrotory already exists" });
  //   }
  // } catch (err) {
  //   console.error(err);
  // } finally {
  // }

};

module.exports = {
  getLab,
  postLab,
};
