import React, { useState, useRef } from "react";
import path from "path";
import { Editor } from "@tinymce/tinymce-react";
import axios from "axios";
import { makeStyles } from "@material-ui/core/styles";
import ArrowBackIcon from "@material-ui/icons/ArrowBack";
import Snackbar from "@material-ui/core/Snackbar";
import MuiAlert from "@material-ui/lab/Alert";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import Swal from 'sweetalert2'
import { nanoid } from "nanoid";
import { Button } from "@material-ui/core";
import "./procedure.css";
import ApiUrl from "../../../ServerApi";
function Alert(props) {
  return <MuiAlert elevation={6} variant="filled" {...props} />;
}

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    marginTop: "-1%",
    width: "85%",
    "& > * + *": {
      marginTop: theme.spacing(5),
      marginLeft: theme.spacing(5),
    },
  },
}));

const App = (props) => {
  const classes = useStyles();
  const titleRef = useRef("");
  const labRef = useRef("");
  const departmentRef = useRef("");
  const yearRef = useRef("");
  const collegeRef = useRef("");
  const [state, setState] = useState({ content: "" });
  const [open, setOpen] = useState(false);
  const [message, setMessage] = useState(null);
  const [showResults, setShowResults] = useState(false);
  const onClickshow = (e) => {
    e.preventDefault();
    return setShowResults((prev) => !prev);
  };
  const Search = () => {
   
    return (
      <div>
        <Button variant="contained"  type="submit" style={{ backgroundColor:"#F1C232",color:"black",position:"absolute",top: 65, right: 100,}} onClick={onClickshow}>
        {showResults ? "HIDE" : "SHOW"}
        </Button>
       
        {showResults ? <Results /> : null}
      </div>
    );
  };

  const Results = () => (
    <Card className="blocks" style={{ backgroundColor: "#E7E9EB",position:"absolute",top:"120px",zIndex:10}}>
      <CardContent>
        <input
          className="title"
          placeholder="Experiment Title"
          type="text"
          ref={titleRef}
        />
        <br />
        <br />
        <input
          className="lab"
          placeholder="Lab Type"
          type="text"
          ref={labRef}
        />
        <br />
        <br />
        <input
          className="department"
          placeholder="Department"
          type="text"
          ref={departmentRef}
        />
        <br />
        <br />
        <input className="year" placeholder="Year" type="text" ref={yearRef} />
        <br />
        <br />
        <input
          className="college"
          placeholder="College"
          type="text"
          ref={collegeRef}
        />
        <br />
        <br />
        <input
          button
          type="submit"
          value="save"
          style={{ position: "center", backgroundColor:"#F1C232" }}
        />
      </CardContent>
    </Card>
  );

  const handleClose = (event, reason) => {
    if (reason === "clickaway") {
      return;
    }

    setOpen(false);
  };

  const handleEditorChange = (e) => {
    console.log("Content was updated:", e.target.getContent());
  };
  const handleSave = (e) => {
    e.preventDefault();
    // /moreInfo

    axios
      .post(`${ApiUrl}/procedures`, {
        title: titleRef.current.value,
        html: e.target.getContent(),
      })
      .then((res) => {
        axios
          .post(`${ApiUrl}/moreInfo`, {
            experimentno: res.data._id,
            experiment: titleRef.current.value,
            lab: labRef.current.value,
            department: departmentRef.current.value,
            year: yearRef.current.value,
            college: collegeRef.current.value,
          })
          .then(() => {
            console.log("sent meta info");    
            // axios.post(`${ApiUrl}/labrotories`, {
            //   name: labRef.current.value,
            //   experiment: titleRef.current.value,
            // })
            Swal.fire(
              'success',
              'Procedure has been updated',
              'success',
            )
            setShowResults((prev) => !prev)
          })
          .catch((err) => {
            console.error(err)
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Something went wrong Check your internet connection',
           
            })
        
          });

        // setMessage("Template saved successfully.");
        setOpen(true);
     
      });
  };
  const handleChange = (content, editor) => {
    setState({ content });
  };
  const handleSubmit = (e) => {
    e.preventDefault();
  };
  const goBack = () => {
    props.history.push("/procedure");
  };
  return (
    <div className={classes.root}>
      <ArrowBackIcon
        onClick={goBack}
        style={{
          color: "red",
          border: "1px solid black",
          borderRadius: "50%",
          background: "white",
          zIndex: 100000,
          position: "absolute",
          top: 10,
          right: 30,
        }}
      />

      <Snackbar open={open} autoHideDuration={3000} onClose={handleClose}>
        <Alert onClose={handleClose} severity="success">
          {message}
        </Alert>
      </Snackbar>

      <form method="POST" onSubmit={handleSubmit}>
        <Search />

        <Editor
          id="myTiny_Mce"
          initialValue="<p>Initial content</p>"
          apiKey="au50u78j9vjabzcr4icg4v3oknubu08ifv9rfstawlzmdobp"
          init={{
            height: "90vh",
            menubar: true,
            selector: "textarea",
            external_plugins: {
              tiny_mce_wiris: `${path.join(
                __dirname,
                "../../../../node_modules/@wiris/mathtype-tinymce5/plugin.min.js"
              )}`,
            },
            plugins: [
              "advlist autolink lists link image code textpattern template",
              "charmap print preview anchor help",
              "searchreplace visualblocks code",
              "insertdatetime media table advtablesort paste wordcount save",
            ],
            toolbar: `undo redo | formatselect | bold italic | \
            alignleft aligncenter alignright | \
            bullist numlist outdent indent | help | image code table customInsertButton customDateButton template tiny_mce_wiris_formulaEditor tiny_mce_wiris_formulaEditorChemistry`,
            image_advtab: true,
            image_title: true,
            automatic_uploads: true,
            file_picker_types: "image",
            file_picker_callback: function (cb, value, meta) {
              var input = document.createElement("input");
              input.setAttribute("type", "file");
              input.setAttribute("accept", "image/*");
              input.onchange = function () {
                var file = this.files[0];

                var reader = new FileReader();
                reader.onload = function () {
                  var id = "blobid" + new Date().getTime();
                  var blobCache =
                    window.tinymce.activeEditor.editorUpload.blobCache;
                  var base64 = reader.result.split(",")[1];
                  var blobInfo = blobCache.create(id, file, base64);
                  blobCache.add(blobInfo);
                  cb(blobInfo.blobUri(), { title: file.name });
                };
                reader.readAsDataURL(file);
              };

              input.click();
            },
            setup: function (editor) {
              editor.ui.registry.addButton("customInsertButton", {
                icon: "edit-block",
                tooltip: "Insert Input Element",
                onAction: function (_) {
                  const value = nanoid(7);
                  editor.insertContent(
                    `&nbsp;<input type='text' id='value_${value}' name='value_${value}'>&nbsp;`
                  );
                },
              });

              var toTimeHtml = function (date) {
                return (
                  '<time datetime="' +
                  date.toString() +
                  '">' +
                  date.toDateString() +
                  "</time>"
                );
              };

              editor.ui.registry.addButton("customDateButton", {
                icon: "insert-time",
                tooltip: "Insert Current Date",
                disabled: true,
                onAction: function (_) {
                  editor.insertContent(toTimeHtml(new Date()));
                },
                onSetup: function (buttonApi) {
                  var editorEventCallback = function (eventApi) {
                    buttonApi.setDisabled(
                      eventApi.element.nodeName.toLowerCase() === "time"
                    );
                  };
                  editor.on("NodeChange", editorEventCallback);

                  /* onSetup should always return the unbind handlers */
                  return function (buttonApi) {
                    editor.off("NodeChange", editorEventCallback);
                  };
                },
              });
            },
            content_style:
              "body { font-family:Helvetica,Arial,sans-serif; font-size:14px }",
          }}
          value={state.content}
          onChange={handleEditorChange}
          onEditorChange={handleChange}
          onSaveContent={handleSave}
        />

        {/* <div className="watermark"></div> */}
      </form>
    </div>
  );
};

export default App;
