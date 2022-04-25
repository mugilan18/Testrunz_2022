const Note = require("../models/Note");

const getAll = async function (req, res, next) {
  try {
    const notes = await Note.find();
    res.json(notes);
  } catch (err) {
    console.error(err);
  }

  // res.json({ message: "respond with a resource" });
};

const getById = async function (req, res, next) {
  try {
    const note = await Note.findOne({ runID: req.params.runID });
    res.json(note);
  } catch (err) {
    console.error(err);
  }
};

const postNote = function (req, res, next) {
  const newNote = new Note({
    runID: req.body.runID,
    notes: req.body.notes,
  });
  newNote
    .save()
    .then((result) => res.json(result))
    .catch((err) => console.error(err));
};

const patchNotes = async (req, res) => {
  try {
    const updatedNote = await Note.findOneAndUpdate(
      { runID: req.params.runID },
      {
        $set: {
          notes: req.body.notes,
        },
      }
    );
    res.json(updatedNote);
  } catch (err) {
    console.error(err);
  }
};

const deleteNotes = async (req, res) => {
  try {
    const removedNote = await Note.remove({ runID: req.params.runID });
    res.json(removedNote);
  } catch (err) {
    console.error(err);
  }
};

module.exports = { getAll, getById, postNote, patchNotes, deleteNotes };
