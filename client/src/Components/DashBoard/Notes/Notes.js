import React from "react";
import axios from "axios";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css";
import ApiUrl from "../../../ServerApi";
import Button from "@material-ui/core/Button";


const modules = {
  toolbar: [
    [{ header: [1, 2, false] }],
    ["bold", "italic", "underline", "strike", "blockquote"],
    [
      { list: "ordered" },
      { list: "bullet" },
      { indent: "-1" },
      { indent: "+1" },
    ],
    ["link", "image"],
    ["clean"],
  ],
};

const formats = [
  "header",
  "bold",
  "italic",
  "underline",
  "strike",
  "blockquote",
  "list",
  "bullet",
  "indent",
  "link",
  "image",
];

const Notes = ({ data }) => {
  const [dataV, setDataV] = React.useState("");

  React.useEffect(() => {
    async function fetchData() {
      await axios
        .get(`${ApiUrl}/notes/${data.runID}`, { headers: {} })
        .then((res) => setDataV(res.data.notes));
    }

    if (data.runID) fetchData();
  }, [data.runID]);

  const saving = async () => {
    await axios.patch(`${ApiUrl}/notes/${data.runID}`, {
      notes: dataV,
    });
  };
  //console.log(dataV);
  return (
    <>
      <Button onClick={saving} variant="contained" style={{background:"#3F51B5",color:"#fff"}}>Save</Button>
      <br/>
      <br/>
      <br/>
      <ReactQuill
        theme="snow"
        modules={modules}
        formats={formats}
        value={dataV.replace(/['"]+/g, "")}
        onChange={setDataV}
      />
    </>
  );
};

export default Notes;
