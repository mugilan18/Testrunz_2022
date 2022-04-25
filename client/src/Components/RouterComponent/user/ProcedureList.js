import React, { useEffect, useState } from "react";

import axios from "axios";


import { useStateValue } from '../../../data/StateProvider';
import { actionTypes } from "../../../data/reducer"

import MuiAlert from "@material-ui/lab/Alert";
import { makeStyles } from "@material-ui/core/styles";
import MaterialTable from 'material-table';
import Loading from "./Lodaing"
import { useHistory } from "react-router-dom";

import ApiUrl from "../../../ServerApi"
function Alert(props) {
  return <MuiAlert elevation={6} variant="filled" {...props} />;
}

const useStyles = makeStyles((theme) => ({
  root: {
    width: "100%",
    height: "100%",
    "& > * + *": {
      marginTop: theme.spacing(2),
    },
  },
}));

const Procedurelist = () => {
  const [dat, setDat] = useState(null);
  const classes = useStyles();
  const [loadingscreen, setLoadingscreen] = useState(true)
  const history = useHistory()

  const [{ user }, dispatch] = useStateValue();
  const columns1 = [
    { title: "ID", field: "id" },
    { title: "Procedure Name", field: "ProcedureName" },
    { title: "Lab Name", field: "labtype" },
    { title: "Department", field: "department" },
    { title: "Year", field: "year" },
    { title: "College", field: "college" },

  ];

  useEffect(() => {
    if (user.role == "superadmin") {
      fetch(`${ApiUrl}/moreInfo`)
        .then(data => data.json())
        .then(data => {
          setDat(data.data)
          setLoadingscreen(false)
        })
    }

    else {
      let lab = user.labtype
      fetch(`${ApiUrl}/moreInfo/selected`, {
        method: "POST",
        body: JSON.stringify({
          lab:lab
        }),
        headers: {
          "Content-type": "application/json; charset=UTF-8"
        }
      })
        .then(data => data.json())
        .then(data => {
          setDat(data.data)
          setLoadingscreen(false)
        })
    }



  }, []);

  const addProc = () => {
    // window.localStorage.clear();
    history.push("/addProce");
  };

  const editProc = (id) => {
    // window.localStorage.clear();
    axios.get(`${ApiUrl}/moreInfo/${id}`).then((res) => {
      window.localStorage.setItem("proceId", res.data.id);

    });
    dispatch({
      type: actionTypes.SET_PROSID,
      prosid: id,
    });

    history.push(`/editProce/${id}`);
  };

  return (
    <div className={classes.root}>




      <div style={{ maxWidth: '100%' }}>
        {loadingscreen ? <Loading /> :
          <MaterialTable


            columns={columns1}
            data={dat}
            title="Procedures"
            onRowClick={(e, data) => editProc(data.id)}
            options={{
              // actionsColumnIndex: -1, grouping:true, 
              pageSizeOptions: [5, 10], pageSize: 5
            }}

            actions={[
              {
                icon: 'add',
                tooltip: 'Add Procedure',
                isFreeAction: true,
                onClick: () => addProc()
              }
            ]}

          />
        }
      </div>

    </div>
  );
};

export default Procedurelist;













































// {dat && dat.data.data ? (
//   <DataGrid
//     pagination
//     columns={[
//       {
//         field: "id",
//         headerName: "id",
//         description: "The identification used Procedure Sequence.",
//         width: 100,
//       },
//       {
//         field: "ProcedureName",
//         headerName: "Procedure Name",
//         width: 190,
//       },
//       { field: "labtype", headerName: "Lab Type", width: 170 },

//       {
//         field: "department",
//         headerName: "department",
//         width: 170,
//       },
//       { field: "year", headerName: "year", width: 170 },
//       { field: "college", headerName: "college", width: 170 },
//       {
//         field: "editProcedure",
//         headerName: "Edit Procedure",
//         width: 200,
//         disableClickEventBubbling: true,
//         renderCell: (params) => {
//           const onClick = () => {
//             const api = params.api;

//             const fields = api
//               .getAllColumns()
//               .map((c) => c.field)
//               .filter((c) => c !== "__check__" && !!c);

//             const thisRow = {};
//             fields.forEach((f) => {
//               thisRow[f] = params.row?.[f];
//             });

//             return editProc(thisRow["id"]);
//           };
//           return <Button onClick={onClick}>Edit</Button>;
//         },
//       },
//     ]}
//     rows={dat.data.data}
//   />
// ) : null}