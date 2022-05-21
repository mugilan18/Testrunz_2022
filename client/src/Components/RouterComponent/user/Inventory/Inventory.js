
import { Autocomplete, Button, TextField } from "@mui/material";
import React, { useState } from "react";
import Chip from '@mui/material/Chip';
import ApiUrl from "../../../../ServerApi";
import UploadFileIcon from '@mui/icons-material/UploadFile';
import * as XLSX from "xlsx";
import Grid from '@mui/material/Grid';
import List from '@mui/material/List';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import ListItemIcon from '@mui/material/ListItemIcon';
import Checkbox from '@mui/material/Checkbox';
import ApiService from "../../../../Sevices/ApiService";
import { useStateValue } from "../../../../data/StateProvider";
import Divider from '@mui/material/Divider';

function not(a, b) {
  return a.filter((value) => b.indexOf(value) === -1);
}

function intersection(a, b) {
  return a.filter((value) => b.indexOf(value) !== -1);
}

function union(a, b) {
  return [...a, ...not(b, a)];
}

function Inventory() {
  const [emaillist, setEmaillist] = useState([]);
  const [newemail,setNewemail]=useState()
  const [{ user }, dispatch] = useStateValue();


  const [checked, setChecked] = React.useState([]);
  const [right, setRight] = React.useState([]);
  const [lab,setLab]=useState()
  const [explist,setExplist]=useState([])
  const [experiment,setExperiment]=useState()


  const leftChecked = intersection(checked, emaillist);
  const rightChecked = intersection(checked, right);

  const handleToggle = (value) => () => {
    const currentIndex = checked.indexOf(value);
    const newChecked = [...checked];

    if (currentIndex === -1) {
      newChecked.push(value);
    } else {
      newChecked.splice(currentIndex, 1);
    }

    setChecked(newChecked);
  };

  const numberOfChecked = (items) => intersection(checked, items).length;

  const handleToggleAll = (items) => () => {
    if (numberOfChecked(items) === items.length) {
      setChecked(not(checked, items));
    } else {
      setChecked(union(checked, items));
    }
  };

  const handleCheckedRight = () => {
    setRight(right.concat(leftChecked));
    setEmaillist(not(emaillist, leftChecked));
    setChecked(not(checked, leftChecked));
  };

  const handleCheckedLeft = () => {
    setEmaillist(emaillist.concat(rightChecked));
    setRight(not(right, rightChecked));
    setChecked(not(checked, rightChecked));
  };



  const customList = (title, items) => (
    <Card>
      <CardHeader
        sx={{ px: 2, py: 1 }}
        avatar={
          <Checkbox
            onClick={handleToggleAll(items)}
            checked={numberOfChecked(items) === items.length && items.length !== 0}
            indeterminate={
              numberOfChecked(items) !== items.length && numberOfChecked(items) !== 0
            }
            disabled={items.length === 0}
            inputProps={{
              'aria-label': 'all items selected',
            }}
          />
        }
        title={title}
        subheader={`${numberOfChecked(items)}/${items.length} selected`}
      />
      <Divider />
      <List
        sx={{
          width: 200,
          height: 230,
          bgcolor: 'background.paper',
          overflow: 'auto',
        }}
        dense
        component="div"
        role="list"
      >
        {items.map((value) => {
          const labelId = `transfer-list-all-item-${value}-label`;

          return (
            <ListItem
              key={value}
              role="listitem"
              button
              onClick={handleToggle(value)}
            >
              <ListItemIcon>
                <Checkbox
                  checked={checked.indexOf(value) !== -1}
                  tabIndex={-1}
                  disableRipple
                  inputProps={{
                    'aria-labelledby': labelId,
                  }}
                />
              </ListItemIcon>
              <ListItemText id={labelId} primary={value} />
            </ListItem>
          );
        })}
        <ListItem />
      </List>
    </Card>
  );








  const readExcel = (file) => {
    const promise = new Promise((resolve, reject) => {
      const fileReader = new FileReader();
      fileReader.readAsArrayBuffer(file);

      fileReader.onload = (e) => {
        const bufferArray = e.target.result;

        const wb = XLSX.read(bufferArray, { type: "buffer" });

        const wsname = wb.SheetNames[0];

        const ws = wb.Sheets[wsname];

        const data = XLSX.utils.sheet_to_json(ws);

        resolve(data);
      };

      fileReader.onerror = (error) => {
        reject(error);
      };
    });

    promise.then((d) => {
     
      var names = d.map(function(name) {
        return name['Email'];
      });
      var temp = [...names, ...emaillist]
     var uniqueemail = [...new Set(temp)];
      // setItems(names);
      setEmaillist(uniqueemail)
      
      
      console.log(names)
    });
  };

  const addemail=()=>{
    var temp = [...emaillist,newemail]
     var uniqueemail = [...new Set(temp)];
      // setItems(names);
      setEmaillist(uniqueemail)

  }

  const removeemail=(email)=>{
    var filtered = emaillist.filter((item)=>{return(item!=email)});
setEmaillist(filtered)
  }




  const fetchexperiment = (newValue) => {
    setLab(newValue)
    fetch(`${ApiUrl}/moreInfo/experiment`, {
      method: "POST",
   
      body: JSON.stringify({
        lab: newValue
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8"
    }
  })
  .then(response => response.json())
  .then(json => 
    {

      setExplist(json.ids)

   console.log(json)
    }
    );
  }



  const assign=()=>{
    let value = {
      email: right,
      procedureDescription: `new ${experiment}`,
      labType: lab,
      experimentName: experiment,
      assignedby:user.email
    };
    ApiService.addBulkuser(value)
  .then(res => console.log(res));

  }












  return (
    <div>
     {/* <span style={{paddingLeft:"50px",paddingRight:"50px"}}></span> */}
    <input
    style={{paddingBottom:"10px",}}
        type="file"
        accept=".xlsx,.xls"
        onChange={(e) => {
          const file = e.target.files[0];
          readExcel(file);
        }}
      />
    
    
      
    
     <span style={{paddingLeft:"50px",paddingRight:"50px"}}>
  
      Add Email: <TextField size="small" value={newemail} onChange={e=>setNewemail(e.target.value)}/>     
      </span>
      <Button variant="contained" onClick={addemail}>add email</Button>
      <br/> <br/> <br/><br/>
     <Grid container spacing={2} justifyContent="center" alignItems="center">
      <Grid item>{customList('Choices', emaillist)}</Grid>
      <Grid item>
        <Grid container direction="column" alignItems="center">
          <Button
            sx={{ my: 0.5 }}
            variant="outlined"
            size="small"
            onClick={handleCheckedRight}
            disabled={leftChecked.length === 0}
            aria-label="move selected right"
          >
            &gt;
          </Button>
          <Button
            sx={{ my: 0.5 }}
            variant="outlined"
            size="small"
            onClick={handleCheckedLeft}
            disabled={rightChecked.length === 0}
            aria-label="move selected left"
          >
            &lt;
          </Button>
        </Grid>
      </Grid>
      <Grid item>{customList('Chosen', right)}</Grid>

      <Grid item>
      <Autocomplete
    style={{padding:"10px"}}
            id="outlined-basic"
            variant="outlined"
            size="small"
            value={lab}
            onChange={(event, newValue) => {
              fetchexperiment(newValue)
              setExperiment();

            }}
            options={user.labtype.map((option) => option)}
            sx={{ width: 300 }}
            renderInput={(params) => <TextField {...params} />}
          />
<Autocomplete
style={{padding:"10px"}}
        id="outlined-basic"
        variant="outlined"
        size="small"
        value={experiment}
        onChange={(event, newValue) => {
          setExperiment(newValue);
        }}
        options={explist.map((option) => option)}
        // options={options}
        sx={{ width: 300 }}
        renderInput={(params) => <TextField {...params} />}
      />

      </Grid>


    </Grid>
    <br/><br/>
   
    
<Button onClick={assign}>assign</Button>
    </div>
  );
}


export default Inventory