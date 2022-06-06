import Divider from "@mui/material/Divider";
import Paper from "@mui/material/Paper";
import MenuList from "@mui/material/MenuList";
import MenuItem from "@mui/material/MenuItem";
import ListItemText from "@mui/material/ListItemText";
import ListItemIcon from "@mui/material/ListItemIcon";
import Typography from "@mui/material/Typography";
import ContentCut from "@mui/icons-material/ContentCut";
import ContentCopy from "@mui/icons-material/ContentCopy";
import ContentPaste from "@mui/icons-material/ContentPaste";
import Cloud from "@mui/icons-material/Cloud";
import List from '@mui/material/List';
import ListSubheader from '@mui/material/ListSubheader';
import { styled } from '@mui/material/styles';

import ListItemButton from '@mui/material/ListItemButton';

import Collapse from '@mui/material/Collapse';
import DraftsIcon from '@mui/icons-material/Drafts';
import SendIcon from '@mui/icons-material/Send';
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import StarBorder from '@mui/icons-material/StarBorder';

import MaterialTable from 'material-table'
import "./Support.css";
import { Link } from "react-scroll";

import logo from "./images/template.png";


import figs_1 from "./images/figs_1.png";
import figs_2 from "./images/figs_2.png";
import figs_3 from "./images/figs_3.png";
import figs_4 from "./images/figs_4.png";
import figs_5 from "./images/figs_5.png";
import figs_6 from "./images/figs_6.png";
import figs_7 from "./images/figs_7.png";
import figs_8 from "./images/figs_8.png";
import figs_9 from "./images/figs_9.png";

import figt_1 from "./images/figt_1.png";
import figt_2 from "./images/figt_2.png";
import figt_3 from "./images/figt_3.png";
import figt_4 from "./images/figt_4.png";
import figt_5 from "./images/figt_5.png";
import figt_6 from "./images/figt_6.png";
import figt_7 from "./images/figt_7.png";
import figt_8 from "./images/figt_8.png";
import figt_9 from "./images/figt_9.png";

import figa_1 from "./images/figa_1.png";
import figa_2 from "./images/figa_2.png";
import figa_3 from "./images/figa_3.png";
import figa_4 from "./images/figa_4.png";
import figa_5 from "./images/figa_5.png";
import figa_6 from "./images/figa_6.png";
import figa_7 from "./images/figa_7.png";
import figa_8 from "./images/figa_8.png";
import figa_9 from "./images/figa_9.png";
import figlo from "./images/figlo.png";
import editpros from "./images/editpro.png";
import inventory from "./images/inventory.png";
import figsa_1 from "./images/figsa_1.png";
import figsa_2 from "./images/figsa_2.png";
import figsa_3 from "./images/figsa_3.png";
import figsa_4 from "./images/figsa_4.png";
import figsa_5 from "./images/figsa_5.png";
import figsa_6 from "./images/figsa_6.png";
import figsa_7 from "./images/figsa_7.png";
import figsa_8 from "./images/figsa_8.png";
import figsa_9 from "./images/figsa_9.png";

import * as React from "react";
import Box, { BoxProps } from "@mui/material/Box";
import Grid from '@mui/material/Grid';



const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
  // ...theme.typography.body2,
  padding: theme.spacing(1),
  // textAlign: 'center',
  color: theme.palette.text.secondary,
}));
const drawerWidth = 200;

const Helpguide1 = () => {
  const [openstudent,setOpenstudent]=React.useState(false)
  const [openteacher,setOpenteacher]=React.useState(false)
  const [openadmin,setOpenadmin]=React.useState(false)
  const [opensuperadmin,setOpensuperadmin]=React.useState(false)

  return (
    <Grid container >
        <Grid item xs={10}>
      <Item >
        <div>
          <section style={{ display: "block" }}>
            <div style={{fontSize:'40px'}}>Welcome to the TestRunz Documentation</div>
            <br />
            <h2>Find the guides, sample images, and references you need to use, calculate data, and study experiment on the testrunz platform.</h2>
            <div>
              <img
                style={{ width: "100%", height: "300px",  display: "block", marginLeft: "auto",  marginRight: "auto",marginTop:"100px" }}
                src={logo}
                alt=""
              /><br/>
              
            </div>
          </section>

          <section style={{ display: "block" }} id="access">
            <h2>Access Control</h2>
            <br />
            <MaterialTable
          columns={[
            { title: 'Page', field: 'page' },
            { title: 'Super Admin', field: 'superadmin' },
            { title: 'Admin', field: 'admin' },
            { title: 'Teacher', field: 'teacher' },
            { title: 'Student', field: 'student' },
             ]}
        
          data={[
            { page: 'My Page', superadmin: 'Access', admin: 'Access', teacher: 'Access',student:'Access' },
            { page: 'Run', superadmin: 'Access', admin: "Access", teacher: "Access",student:"Access" },
            { page: 'Edit produce', superadmin: 'Access', admin: "view", teacher: "view" ,student:"view"},
            { page: 'Add user', superadmin: 'Access', admin: "Access", teacher: "Access" ,student:"Access"},
            { page: 'Inventory', superadmin: 'Access', admin: "Access", teacher: "Access" ,student:"No Access"},
            { page: 'Setting', superadmin: 'Access', admin: "Access", teacher: "Access" ,student:"No Access"},
            { page: 'Support', superadmin: 'Access', admin: "Access", teacher: "Access",student:"Access" },
            { page: 'Profile', superadmin: 'Access', admin: "Access", teacher: "Access",student:"Access" },
                  ]}
          title="Page Access"
          options={{
            paging: false,search: false
          }}
        />
          </section>

          <section style={{ display: "block" }} id="signup">
            <div>
              <h2>SIGN UP:</h2>
            </div>

            <p>Users can sign up for the system as follows.</p>
            <ol>
              <li>
                <p>
                  Go to the testRunz website:
                  <a href="#/">http://testrunz.com/#/</a>
                </p>
              </li>
              <li>
                <p>
                  Enter the user name, email address, and password to signup in
                </p>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%",objectFit: "contain" }}
                src={figs_1}
                alt=""
              /><br/>
              
            </div>
          </section>

          <section id="profile" style={{ display: "block" }}>
            <h2>Profile</h2>
            <ol>
              <li>
                <p>Go to the profile page</p>
              </li>
              <li>
                <p>Click the edit option you can edit your profile page</p>
              </li>
              <li>
                <p>
                  Now you can edit your country name, state name, and year and
                  semester on the profile page.
                </p>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%",objectFit: "contain" }}
                src={figs_2}
                alt=""
              />
            </div>
         
            
          </section>

          <section id="mypage" style={{ display: "block" }}>
            <h2>My page</h2>
            <ol>
              <li>
                <p>A list of experiments will be shown</p>
              </li>
              <li>
                <p>
                  Users can search experiments with respect to their&nbsp; 
                  <strong>
                    Id/pProcedure name/Lab name/Submitted by/Submitted time&nbsp;
                  </strong>
                  using the search input tag.
                </p>
              </li>
              <li>
                <p>
                  On clicking the experiment, the user can see the content and
                  values in the tabular column , which the sender fills.
                </p>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", objectFit: "contain"}}
                src={figs_3}
                alt=""
              />
            </div>
            <br />
            <br />
            <br />
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", objectFit: "contain"}}
                src={figs_4}
                alt=""
              />
            </div>
          </section>

          <section id="runz" style={{ display: "block" }}>
            <h2>Runz</h2>
            <ol>
              <li>
                <p>
                  Users can search experiments with respect to their&nbsp;
                  <strong>
                    Id/Procedure name/Lab name/Submitted by/Submitted time&nbsp;
                  </strong>
                  using the search input tag.
                </p>
              </li>
            </ol>

            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", objectFit: "contain"}}
                src={figs_5}
                alt=""
              />
            </div>

            <ol>
              <li>
                <p>
                  Click the * <strong>+ *</strong>option in the top right corner
                  of the runz table, which opens the Add Runz modal.
                </p>
              </li>
              <li>
                <p>
                  Enter the <strong>Experiment description </strong>and select
                  the Lab type, Procedure name also in the given order.
                </p>
              </li>
              <li>
                <p>
                  Click the <strong>save</strong> to create a runz.
                </p>
              </li>
            </ol>

            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%",objectFit: "contain" }}
                src={figs_6}
                alt=""
              />
            </div>
          </section>

          <section id="procedure" style={{ display: "block" }}>
            <h2>Procedure</h2>
            <strong style={{color:"red"}}> &nbsp;&nbsp;*Only Super Adim has access to create or edit procedure*</strong>
            <br/><br/>
            <ol>
              <li>
                <p>
                  <strong>Admin, Teacher and Student: </strong> The procedure page displays the list of experiments that can
                  be accessed by the User.
                  
                </p>
              </li>
              <li>
                <p>
                <strong>Super Admin: </strong> The procedure page displays the list of experiments that can
                  be accessed by the user, Super admin has access to each procedure where they can edit the existing procedure or they can create a new procedure.
                </p>
              </li>
              
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%",objectFit: "contain" }}
                src={figs_7}
                alt=""
              />
            </div>
            <br />
            <br />
            <br />
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%",objectFit: "contain" }}
                src={editpros}
                alt=""
              />
            </div>
          </section>

          {/* <section id="inventory" style={{ display: "block" }}>
            <h2>Inventory</h2>
            <br/>
            <ol>
              <li>
                <p>
                  Staff can assign experiment to students in bulk by adding runz to students account individually.
                </p>
              </li>
              <li>
                <p>
                  The Students email can be imported from excel sheet. <strong> *The heading of the Sheet must be "Email"*</strong>
                </p>
              </li>
              <li>
                <p>Once imported, the list of Emails are visible in the choices box. </p>
              </li>
              <li>
                <p>Students email can also be added manually using the Email input box. </p>
              </li>
              <li>
                <p>User can select specific number of student in chosen box and assign the respective labs using drop down. </p>
              </li>
            </ol>
          

            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", objectFit: "contain"}}
                src={inventory}
                alt=""
              />
            </div>
          </section> */}

          <section id="adduser" style={{ display: "block" }}>
            <h2>Add User</h2>
            <ol>
              <li>
                <p>
                  User can create accounts for other user in Add user page.
                </p>
              </li>
              <li>
                <p>
  
                  User should Enter the other user name and email address to whom they want to create account, on add user
                  page and select the role.
                  
                </p>
              </li>
              <li>
                <p>Finally, click the create user Button</p>
              </li>
            </ol>
            <ul>
       
              <li>
                <p>Student can creacte account for <strong>Student</strong> only</p>
              </li>
              <li>
                <p>Teacher can creacte account for <strong>Student</strong> only also can assign lab</p>
              </li>
              <li>
                <p>Admin can creacte account for <strong>Student</strong> and <strong>Teacher</strong> also can assign lab within the department </p>
              </li>
              <li>
                <p>Super Admin can creacte account for <strong>Student</strong>, <strong>Teacher</strong> and <strong>Admin</strong> also can assign department and lab</p>
              </li>
            </ul>

            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%",objectFit: "contain" }}
                src={figs_8}
                alt=""
              />
            </div>
          </section>

          <section id="support" style={{ display: "block" }}>
            <h2>Support</h2>
            <ol>
              <li>
                <p>User can give their feedback here.</p>
              </li>
              <li>
                <p>
                  User can list the bugs or features or even in their
                  comments in the input tag and specify the feedback category.
                </p>
              </li>
              <li>
                <p>User also can upload the image more specifically.</p>
              </li>
            </ol>

            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%",objectFit: "contain" }}
                src={figs_9}
                alt=""
              />
            </div>
          </section>

          <section id="setting" style={{ display: "block" }} >
          <h2>Setting</h2>
          <strong style={{color:"red"}}> &nbsp;&nbsp;*Student has no access to this page*</strong>
          <ol>
            <li>
              <p>Click the setting option</p>
            </li>
            <li>
              <p>
                In the Manage user section, Admin can able to view/edit/update
                the list of students/teacher;s role/country/ year/semester/access
                lab sections.
              </p>
            </li>
            <li>
              <p>
                Enter the search option in the top right corner, now you can
                search any one of these: Name\Email\Role\Id\Country\college name.
              </p>
            </li>
            <li>
              <p>
                Now choose the specific user column to be changed and make changes if any
                changes occur on that account you can able to update and can
                able to add access lab to that account.
              </p>
            </li>
            <li>
              <p>
                Super Admin can edit on&nbsp;
                <strong>
                  Super admin can  edit on Role, country, year, state,
                  semester, and list of labs available
                </strong>
              </p>
              <p>
                Admin can only edit on&nbsp;
                <strong>
                  Role, country, year, state, semester, and list of labs  available 
                </strong>
              </p>
              <p>
                Teacher can only edit on&nbsp;
                <strong>
                Role, country, year, state, semester, and list of labs available
                </strong>
              </p>
            </li>
          </ol>
          <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", objectFit: "contain"}}
                src={figa_8}
                alt=""
              />
            </div>
        </section>

        <section id="logout" style={{ display: "block" }} >
            <h2>Logout :</h2>
            <p>You can log out of the system as follows</p>
            <ol>
              <li>
                <p>Click on the user name icon in the top right corner.</p>
              </li>
              <li>
                <p>Click on the 'LOGOUT' option</p>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%",objectFit: "contain" }}
                src={figlo}
                alt=""
              />
            </div>
        </section>
        </div>
 
        
    
      </Item>
      </Grid>
        <Grid item xs={2}>
      <div  >
        <div style={{position:"fixed" ,width:200}} >
        <Paper style={{maxHeight: "70vh", overflow: 'auto'}}>
  
        <List
        
          sx={{ width: '100%', maxWidth: 400, bgcolor: 'background.paper' }}
          component="nav"
          aria-labelledby="nested-list-subheader"
                   
          
        >
           <ListItemButton >
      
        <ListItemText primary="Contents:" />
       
      </ListItemButton>
<Divider/>

        <List component="div" disablePadding>
        <Link
            activeClass="active"
            to="signup"
            spy={true}
            offset={-100}
            smooth={true}
            duration={500}
          >
            <MenuItem>
              <ListItemText>Sign Up</ListItemText>
            </MenuItem>
          </Link>


          <Link
            activeClass="active"
            to="profile"
            spy={true}
            smooth={true}
            duration={500}
            offset={-100}
          >
            <MenuItem>
              <ListItemText>Edit Profile</ListItemText>
            </MenuItem>
          </Link>


          <Link
            activeClass="active"
            to="mypage"
            spy={true}
            smooth={true}
            duration={500}
            offset={-100}
          >
            <MenuItem>
              <ListItemText>My Page</ListItemText>
            </MenuItem>
          </Link>

          <Link
            activeClass="active"
            to="runz"
            spy={true}
            smooth={true}
            duration={500}
            offset={-100}
          >
            <MenuItem>
              <ListItemText>Runz</ListItemText>
            </MenuItem>
          </Link>

          <Link
            activeClass="active"
            to="procedure"
            spy={true}
            smooth={true}
            duration={500}
            offset={-100}
          >
            <MenuItem>
              <ListItemText>Procedure</ListItemText>
            </MenuItem>
          </Link>

          {/* <Link
            activeClass="active"
            to="inventory"
            spy={true}
            smooth={true}
            duration={500}
            offset={-100}
          >
            <MenuItem>
              <ListItemText>Inventory</ListItemText>
            </MenuItem>
          </Link> */}

          <Link
            activeClass="active"
            to="adduser"
            spy={true}
            smooth={true}
            duration={500}
            offset={-100}
          >
            <MenuItem>
              <ListItemText>Add User</ListItemText>
            </MenuItem>
          </Link>

          <Link
            activeClass="active"
            to="support"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>Support</ListItemText>
            </MenuItem>
          </Link>

          <Link
            activeClass="active"
            to="setting"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>Setting</ListItemText>
            </MenuItem>
          </Link>

          <Link
            activeClass="active"
            to="logout"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>Logout</ListItemText>
            </MenuItem>
          </Link>
        </List>
 




          



  

        </List>
        </Paper>
        </div>
      </div>
      </Grid>
      
      </Grid>
  );
};

export default Helpguide1;
