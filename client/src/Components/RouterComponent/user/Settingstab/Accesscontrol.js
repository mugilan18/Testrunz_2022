  import React, { useEffect, useState } from "react";
  import Checkbox from '@mui/material/Checkbox';
  import Card from '@mui/material/Card';
  import CardActions from '@mui/material/CardActions';
  import CardContent from '@mui/material/CardContent';
  import Grid from '@mui/material/Grid';
  const label = { inputProps: { 'aria-label': 'Checkbox demo' } };
  
  const Accesscontrol = () => {
    const [access,setAccess]=useState({
      subscriber:{read:false,write:false,declined:false,inherited:true},
      student:{read:false,write:false,declined:false,inherited:false},
      teacher:{read:false,write:false,declined:false,inherited:false},
      admin:{read:false,write:false,declined:false,inherited:false},
    })
  
    useEffect(()=>{
      console.log(access)
    })
    return  (
      <Card>
    <CardContent style={{backgroundColor:"#E7EBF0"}}>
  
    Access Management  
    <br/>  <br/>  
  {/* /////////////////////////////////////////// */}
    <Grid container item spacing={3}>
    <Grid item xs={2}>
    Role
    </Grid>
    <Grid item xs={2}>
    Read
    </Grid>
    <Grid item xs={2}>
    Write
    </Grid>
    <Grid item xs={2}>
    Denied
    </Grid>
    <Grid item xs={2}>
    Inherited
    </Grid>
    </Grid>
    <hr/>
  {/* /////////////////////////////////////////// */}
    <Grid container item spacing={3}>
    <Grid item xs={2}>
    Subscriber
    </Grid>
    <Grid item xs={2}>
    <Checkbox 
    checked={access.subscriber.read}
    onChange={(event)=>setAccess({...access,  subscriber: {
      read:event.target.checked,
      inherited:access.subscriber.inherited,
      declined:access.subscriber.declined,
      write:access.subscriber.write,
  
      },
      })}
    {...label} color="success"/>
    </Grid>
    <Grid item xs={2}>
    <Checkbox
    checked={access.subscriber.write}
    onChange={(event)=>setAccess({...access,  subscriber: {
      write:event.target.checked,
      inherited:access.subscriber.inherited,
      declined:access.subscriber.declined,
      read:access.subscriber.read,
      },
      })}
    {...label} color="success"/>
    </Grid>
    <Grid item xs={2}>
    <Checkbox
    checked={access.subscriber.declined}
    onChange={(event)=>setAccess({...access,  subscriber: {
      declined:event.target.checked,
      read:access.subscriber.read,
      write:access.subscriber.write,
      inherited:access.subscriber.inherited,
      },
      })}
    {...label} />
    </Grid>
    <Grid item xs={2}>
    <Checkbox 
    checked={access.subscriber.inherited}
    onChange={(event)=>setAccess({...access,  subscriber: {
      inherited:event.target.checked,
      declined:access.subscriber.declined,
      read:access.subscriber.read,
      write:access.subscriber.write,
      },
      })}
    {...label} color="error"/>
    </Grid>
   
    </Grid>
  {/* /////////////////////////////////////////// */}
    <Grid container item spacing={3}>
    <Grid item xs={2}>
    Student
    </Grid>
    <Grid item xs={2}>
    <Checkbox 
    checked={access.student.read}
    onChange={(event)=>setAccess({...access,  student: {
      read:event.target.checked,
      inherited:access.student.inherited,
      declined:access.student.declined,
      write:access.student.write,
  
      },
      })}
    {...label} color="success"/>
    </Grid>
    <Grid item xs={2}>
    <Checkbox
    checked={access.student.write}
    onChange={(event)=>setAccess({...access,  student: {
      write:event.target.checked,
      inherited:access.student.inherited,
      declined:access.student.declined,
      read:access.student.read,
      },
      })}
    {...label} color="success"/>
    </Grid>
    <Grid item xs={2}>
    <Checkbox
    checked={access.student.declined}
    onChange={(event)=>setAccess({...access,  student: {
      declined:event.target.checked,
      read:access.student.read,
      write:access.student.write,
      inherited:access.student.inherited,
      },
      })}
    {...label} />
    </Grid>
    <Grid item xs={2}>
    <Checkbox 
    checked={access.student.inherited}
    onChange={(event)=>setAccess({...access,  student: {
      inherited:event.target.checked,
      declined:access.student.declined,
      read:access.student.read,
      write:access.student.write,
      },
      })}
    {...label} color="error"/>
    </Grid>
    </Grid>  
  {/* /////////////////////////////////////////// */}
    <Grid container item spacing={3}>
    <Grid item xs={2}>
    Teacher
    </Grid>
    <Grid item xs={2}>
    <Checkbox 
    checked={access.teacher.read}
    onChange={(event)=>setAccess({...access,  teacher: {
      read:event.target.checked,
      inherited:access.teacher.inherited,
      declined:access.teacher.declined,
      write:access.teacher.write,
  
      },
      })}
    {...label} color="success"/>
    </Grid>
    <Grid item xs={2}>
    <Checkbox
    checked={access.teacher.write}
    onChange={(event)=>setAccess({...access,  teacher: {
      write:event.target.checked,
      inherited:access.teacher.inherited,
      declined:access.teacher.declined,
      read:access.teacher.read,
      },
      })}
    {...label} color="success"/>
    </Grid>
    <Grid item xs={2}>
    <Checkbox
    checked={access.teacher.declined}
    onChange={(event)=>setAccess({...access,  teacher: {
      declined:event.target.checked,
      read:access.teacher.read,
      write:access.teacher.write,
      inherited:access.teacher.inherited,
      },
      })}
    {...label} />
    </Grid>
    <Grid item xs={2}>
    <Checkbox 
    checked={access.teacher.inherited}
    onChange={(event)=>setAccess({...access,  teacher: {
      inherited:event.target.checked,
      declined:access.teacher.declined,
      read:access.teacher.read,
      write:access.teacher.write,
      },
      })}
    {...label} color="error"/>
    </Grid>
    </Grid>
  {/* /////////////////////////////////////////// */}
   <Grid container item spacing={3}>
    <Grid item xs={2}>
    Admin
    </Grid>
    <Grid item xs={2}>
    <Checkbox 
    checked={access.admin.read}
    onChange={(event)=>setAccess({...access, admin: {
      read:event.target.checked,
      inherited:access.admin.inherited,
      declined:access.admin.declined,
      write:access.admin.write,
  
      },
      })}
    {...label} color="success"/>
    </Grid>
    <Grid item xs={2}>
    <Checkbox
    checked={access.admin.write}
    onChange={(event)=>setAccess({...access,  admin: {
      write:event.target.checked,
      inherited:access.admin.inherited,
      declined:access.admin.declined,
      read:access.admin.read,
      },
      })}
    {...label} color="success"/>
    </Grid>
    <Grid item xs={2}>
    <Checkbox
    checked={access.admin.declined}
    onChange={(event)=>setAccess({...access,  admin: {
      declined:event.target.checked,
      read:access.admin.read,
      write:access.admin.write,
      inherited:access.admin.inherited,
      },
      })}
    {...label} />
    </Grid>
    <Grid item xs={2}>
    <Checkbox 
    checked={access.admin.inherited}
    onChange={(event)=>setAccess({...access,  admin: {
      inherited:event.target.checked,
      declined:access.admin.declined,
      read:access.admin.read,
      write:access.admin.write,
      },
      })}
    {...label} color="error"/>
    </Grid>
    </Grid>
  
  
  
  
  
  
    </CardContent>
    </Card>
      );
  };
  
  export default Accesscontrol ;