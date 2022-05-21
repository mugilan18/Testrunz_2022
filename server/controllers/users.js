const User = require("../models/Users");
//get (read)
const read = async(req, res, next) => {
  const userID = req.params.id;
  // console.log("user id",req.params._id);
  try {
    const user = await User.findById(userID);
    res.json(user);
    console.log(user)
  } catch (err) {
    console.error(err);
  }

      
   

    }
    // catch((error) => {
    //   if (error) return res.status(400).json({ error: error });
    // });

// update
const update = (req, res, next) => {
  console.log(req.body)
  const {
    collegeName,
    department,
    country,
    state,
    year,
    semester,
    name,
    password,
    _id,
    showOnce,
    role
  } = req.body;
   User.findOne({ _id: _id })
    .then((user) => {
      if (!user) return res.status(400).json({ error: "user not found" });
      user.name = name || user.name;

      if (password) {
        if (password.length < 6) {
          return res
            .status(400)
            .json({ error: "password should be min 6 long" });
        } else {
          user.password = password;
        }
      }
      if (showOnce) {
        user.showOnce = showOnce;
      }
      if (collegeName) {
        user.collegeName = collegeName;
      }
      if (department) {
        user.department = department;
      }
      if (country) {
        user.country = country;
      }
      if (state) {
        user.state = state;
      }
      if (year) {
        user.year = year;
      }
      if (role) {
        user.role = role;
      }
      if (semester) {
        user.semester = semester;
      }
      user
        .save()
        .then((updated) => {
          console.log(updated)
          return res.json({ updated });
        })
        .catch((err) => {
          return res.status(400).json(err);
        });
    })
    .catch((error) => {
      return res.status(400).json(error);
    });
};


const patchlab = async function (req, res, next) {
  lab=req.body.lab

  id=req.body.id
  console.log(role)
  try {
    const updatedContent = await User.findByIdAndUpdate(
      { _id: id },
      {
        $addToSet: { labtype: { $each: lab } },
        
      }
    );
    res.json(updatedContent);
  } catch (err) {
    console.error(err);
    res.json("error");
  }

}


// const patchlabadmin = async function (req, res, next) {
//   id=req.body.id

//   department=req.body.department
//   lab=req.body.labtype
//   role=req.body.role
//   console.log(req.body.lab)

//   try {
//     const updatedContent = await User.findByIdAndUpdate(
//       { _id: id },
//       {
//         $addToSet: { labtype: { $each: lab } },
//         $set: { 
//           // labtype:lab,
//            role: role,
//            department:department,
//         }
//       }
//     );
//     res.json(updatedContent);
//   } catch (err) {
//     console.error(err);
//     res.json("error");
//   }

// }


const patchlabadmin = async function (req, res, next) {

 let key=Object.keys(req.body)[0]
  let value=Object.values(req.body)[0]
  id=req.body.id
console.log(key,value,id)
 

  try {
    const updatedContent = await User.findByIdAndUpdate(
      { _id: id },
      {
        $set: { 
          // labtype:lab,
          [key]: value,
          
        }
      }
    );
    res.json(updatedContent);
  } catch (err) {
    console.error(err);
    res.json("error");
  }

}



const getaccess = async function (req, res, next) {
  role=req.body.role
  department=req.body.department
  collegeName=req.body.collegeName
  console.log(collegeName)
 
  console.log(role)
  try {
    if(role==="superadmin"){
      const updatedContent = await User.find({$or:[{role:"teacher"},{role:"student"},{role:"admin"}] });
      res.json(updatedContent);
    }
    if(role==="admin"){
      // { $and: [{$or:[{role:"teacher"},{role:"student"}] }, { department:department }  ]}
      const updatedContent = await User.find({ $and: [{$or:[{role:"teacher"},{role:"student"}] }, { department:department }, { collegeName:collegeName }]});
      // const updatedContent = await User.find({$or:[{role:"teacher"},{role:"student"}] });
      res.json(updatedContent);
    }
    if(role==="teacher"){
      const updatedContent = await User.find({ $and:[{role:"student"},{department:department },{collegeName:collegeName}]});
      res.json(updatedContent);
    }
    
  } catch (err) {
    console.error(err);
    res.json("error");
  }

}




















module.exports = { read, update,patchlab ,getaccess, patchlabadmin};
