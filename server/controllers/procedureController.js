const html2json = require("html2json").html2json;
const json2html = require("html2json").json2html;
const Content = require("../models/Content");

const getProcedures = async function (req, res, next) {
  try {
    const PAGE_SIZE = 50;
    const page = parseInt(req.query.page ?? "0");
    const contents = await Content.find()
      .skip(PAGE_SIZE * page)
      .limit(PAGE_SIZE);
    const total = await Content.countDocuments({});
    res.json({ totalPage: Math.ceil(total / PAGE_SIZE), contents });
  } catch (err) {
    console.error(err);
  }
};

const getProcedureById = async function (req, res, next) {
  try {
    const content = await Content.findOne({ _id: req.params._id });
    const { title, html } = content;
    res.json({ title, html });
  } catch (err) {
    console.error(err);
  }
};

const searchTitle = async function (req, res, next) {
  try {
    const content = await Content.findOne({ title: req.params.title });
    const { html } = content;
    res.json({ html });
  } catch (err) {
    console.error(err);
  }
};

const testId = async function (req, res, next) {
  try {
    const content = await Content.findOne({ _id: req.params._id });
    const { title, html } = content;
    res.json({ title, html: json2html(html) });
  } catch (err) {
    console.error(err);
  }
};

const postProcedure = function (req, res, next) {
  const newContent = new Content({
    title: req.body.title,
    html: html2json(req.body.html),
  });
  newContent
    .save()
    .then((content) => res.json(content))
    .catch((err) => console.error(err));
};

const patchProcedure = async (req, res) => {
  // console.log("the content",req.body.content)
  // console.log("the content",req.body.title)
  // console.log("the content",req.body.html)
  try {
    const updatedContent = await Content.findByIdAndUpdate(
      { _id: req.body.content },
      {
        $set: {
          title: req.body.title,
          html: html2json(req.body.html),
        },
      }
    );
    res.json(updatedContent);
  } catch (err) {
    console.error(err);
    res.json("error");
  }
};

 const deleteProcedure = async (req, res) => {
  try {
    const removedContent = await Content.remove({ _id: req.params._id });
    res.json(removedContent);
  } catch (err) {
    console.error(err);
  }
};

module.exports = {
  getProcedures,
  getProcedureById,
  searchTitle,
  testId,
  postProcedure,
  patchProcedure,
  deleteProcedure,
};
     