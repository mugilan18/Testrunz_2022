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
              {/* <div style={{textAlign:"center"}}>fig1</div>  */}
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

          <section style={{ display: "block" }} id="q1">
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
                  (Fig.1)
                </p>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figs_1}
                alt=""
              /><br/>
              <div style={{textAlign:"center"}}>fig1</div> 
            </div>
          </section>

          <section id="q2" style={{ display: "block" }}>
            <h2>Edit PROFILE: Student</h2>
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
                  semester on the profile page(Fig.3).
                </p>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figs_2}
                alt=""
              />
            </div>
         
            
          </section>

          <section id="q3" style={{ display: "block" }}>
            <h2>My page: Student</h2>
            <ol>
              <li>
                <p>A list of experiments will be shown</p>
              </li>
              <li>
                <p>
                  Users can search experiments with respect to their
                  <strong>
                    Id/procedure name/lab name/submitted by/submitted time
                  </strong>
                  using the search input tag(Fig.4).
                </p>
              </li>
              <li>
                <p>
                  On clicking the experiment, the user can see the content and
                  values in the tabular column (Fig.5), which the sender fills.
                </p>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figs_3}
                alt=""
              />
            </div>
            <br />
            <br />
            <br />
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figs_4}
                alt=""
              />
            </div>
          </section>

          <section id="q4" style={{ display: "block" }}>
            <h2>Runz: student</h2>
            <ol>
              <li>
                <p>
                  Users can search experiments with respect to their
                  <strong>
                    Id/procedure name/lab name/submitted by/submitted time
                  </strong>
                  using the search input tag<strong>(Fig.5)</strong>
                </p>
              </li>
            </ol>

            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
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
                  Enter the <strong>experiment description </strong>and select
                  the lab type, Procedure name also in the given order. (Fig 6)
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
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figs_6}
                alt=""
              />
            </div>
          </section>

          <section id="q5" style={{ display: "block" }}>
            <h2>Procedure student role</h2>
            <ol>
              <li>
                <p>
                  The procedure page displays the list of experiments that can
                  be accessed by the students(Fig.7)
                </p>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figs_7}
                alt=""
              />
            </div>
          </section>

          <section id="q6" style={{ display: "block" }}>
            <h2>Add user in the student role</h2>
            <ol>
              <li>
                <p>
                  Students can create accounts for their friends on Add user
                  page.
                </p>
              </li>
              <li>
                <p>
                  Enter the friend&rsquo;s name and email address on add user
                  page and select the role.
                </p>
              </li>
              <li>
                <p>Finally, click the create user Button (Fig.8 )</p>
              </li>
            </ol>

            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figs_8}
                alt=""
              />
            </div>
          </section>

          <section id="q7" style={{ display: "block" }}>
            <h2>Support page in the student role</h2>
            <ol>
              <li>
                <p>Students can give their feedback here.</p>
              </li>
              <li>
                <p>
                  Students can list the bugs or features or even in their
                  comments in the input tag and specify the feedback category.
                </p>
              </li>
              <li>
                <p>Students can upload the image more specifically.</p>
              </li>
            </ol>

            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figs_9}
                alt=""
              />
            </div>
          </section>
        </div>
        {/* /////////////////////////////////////////////////////////////////////////// */}
        <div>
          <section style={{ display: "block" }} id="qt1">
            <h3>Edit your PROFILE in Teacher Role</h3>
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
                  semester on the profile page(Fig.10).
                </p>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figt_1}
                alt=""
              />
            </div>
          </section>



          <section style={{ display: "block" }} id="qt2">
            <h2>My page : Teacher</h2>
            <ol>
              <li>
                <p>A list of experiments will be shown</p>
              </li>
              <li>
                <p>
                  Users can search experiments with respect to their{" "}
                  <strong>
                    Id/procedure name/lab name/submitted by/submitted time{" "}
                  </strong>
                  using the search input tag(Fig.11).
                </p>
              </li>
              <li>
                <p>
                  On clicking the experiment, the user can see the content and
                  values in the tabular column (Fig.12), which the sender fills.
                </p>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figt_2}
                alt=""
              />
            </div>
            <br />
            <br />
            <br />
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figt_3}
                alt=""
              />
            </div>
          </section>


          <section style={{ display: "block" }} id="qt3">
            <h2>Runz : TEACHER</h2>
            <ol>
              <li>
                <p>
                  Users can search experiments with respect to their
                  <strong>
                    Id/ procedure name/lab name/assigned by/description{" "}
                  </strong>
                  using the search input tag<strong> </strong>(Fig.13)
                </p>
              </li>
              <li>
                <p>
                  Click the * <strong>+ *</strong>option in the top right corner
                  of the runz table, which opens the Add Runz modal.
                </p>
              </li>
              <li>
                <p>
                  Enter the <strong>experiment description </strong>and select
                  the lab type, Procedure name also in the given order. (Fig 6)
                </p>
              </li>
              <li>
                <p>
                  Click the <strong>save</strong> to create a runz.
                </p>
              </li>
              <li>&nbsp;</li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figt_4}
                alt=""
              />
            </div>
            <br />
            <br />
            <br />
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figt_5}
                alt=""
              />
            </div>
          </section>

          <section style={{ display: "block" }} id="qt4">
            <ol>
              <li>
                <h2>Procedure page : Teacher</h2>
                <ol>
                  <li>
                    <p>
                      The procedure page displays the list of experiments which
                      can be accessed by the students(Fig.15)
                    </p>
                  </li>
                </ol>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figt_6}
                alt=""
              />
            </div>
          </section>


          <section style={{ display: "block" }} id="qt5">
            <ol>
              <li>
                <h2>Add user: Teacher</h2>
                <ol>
                  <li>
                    <p>
                      Teachers can create accounts for students on Add user page
                    </p>
                  </li>
                  <li>
                    <p>
                      Enter the <strong>student</strong> <strong>name</strong>{" "}
                      and <strong>email</strong> <strong>address</strong> on add
                      user page and select the role.
                    </p>
                  </li>
                  <li>
                    <p>Finally, click the create user Button(Fig.16 )</p>
                  </li>
                </ol>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figt_7}
                alt=""
              />
            </div>
          </section>


          <section style={{ display: "block" }} id="qt6">
            <ol>
              <li>
                <h2>Support page : teacher</h2>
                <ol>
                  <li>
                    <p>Teachers can give their feedback here.</p>
                  </li>
                  <li>
                    <p>
                      Teachers can list the bugs or features in the input tag
                      and specify the feedback category.
                    </p>
                  </li>
                  <li>
                    <p>Teachers can upload the image with more specifically.</p>
                  </li>
                </ol>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figt_8}
                alt=""
              />
            </div>
          </section>


          <section style={{ display: "block" }} id="qt7">
            <ol>
              <li>
                <h2>Setting page : teacher</h2>
                <ol>
                  <li>
                    <p>Click the setting option</p>
                  </li>
                  <li>
                    <p>
                      In the manages user section, Teachers can able to
                      view/edit/update the list of students' role/country/
                      year/semester/access lab.
                    </p>
                  </li>
                  <li>
                    <p>
                      Enter the search option in the top right corner, now you
                      can search: Name\Email\Role\Id\Country\college name.
                    </p>
                  </li>
                  <li>
                    <p>
                      Now choose the selective student column and if any changes
                      occur on that account you can able to update and can able
                      to add access lab to that account.
                    </p>
                  </li>
                  <li>
                    <p>
                      Teachers can only edit on
                      <strong>
                        Role, country, year, state, semester, and list of labs
                        available (
                      </strong>
                      Fig.18)
                    </p>
                  </li>
                </ol>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figt_9}
                alt=""
              />
            </div>
          </section>
        </div>
        {/* ///////////////////////////////////////////// */}
        <div>
          <section style={{ display: "block" }} id="qsa1">
            <ol>
              <li>
                <h3>Edit your PROFILE in Superadmin Role</h3>
                <ol>
                  <li>
                    <p>Go to the profile page</p>
                  </li>
                  <li>
                    <p>Click the edit option you can edit your profile page</p>
                  </li>
                  <li>
                    <p>
                      Now you can edit your college name, department, country,
                      and state name on the profile page(Fig.18).
                    </p>
                  </li>
                </ol>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figsa_1}
                alt=""
              />
            </div>
          </section>


          <section style={{ display: "block" }} id="qsa2">
            <ol>
              <li>
                <h2>My page : Super admin</h2>
                <ol>
                  <li>
                    <p>A list of experiments will be shown</p>
                  </li>
                  <li>
                    <p>
                      Users can search experiments with respect to their{" "}
                      <strong>
                        Id/procedure name/lab name/submitted by/submitted time{" "}
                      </strong>
                      using the search input tag(Fig.19).
                    </p>
                  </li>
                  <li>
                    <p>
                      On clicking the experiment, the user can see the content
                      and values in the tabular column, which the sender fills.
                      (Fig.20)
                    </p>
                  </li>
                </ol>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figsa_2}
                alt=""
              />
            </div>
            <br />
            <br />
            <br />
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figsa_3}
                alt=""
              />
            </div>
          </section>


          <section style={{ display: "block" }} id="qsa3">
            <ol>
              <li>
                <h2>Runz : Super admin</h2>
                <ol>
                  <li>
                    <p>
                      Users can search experiments with respect to their{" "}
                      <strong>
                        Id/ procedure name/lab name/assigned by/description{" "}
                      </strong>
                      using the search input tag(Fig.21)
                    </p>
                  </li>
                  <li>
                    <p>
                      Click the * <strong>+ *</strong>option in the top right
                      corner of the runz table, which opens the Add Runz modal.
                    </p>
                  </li>
                  <li>
                    <p>
                      Enter the <strong>experiment description </strong>and
                      select the lab type, Procedure name also in the given
                      order. (Fig 22)
                    </p>
                  </li>
                  <li>
                    <p>
                      Click the <strong>save</strong> to create a runz.
                    </p>
                  </li>
                </ol>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figsa_4}
                alt=""
              />
            </div>
            <br />
            <br />
            <br />
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figsa_5}
                alt=""
              />
            </div>
          </section>


          <section style={{ display: "block" }} id="qsa4">
            <div>
              <h2>Procedure: Super admin</h2>
            </div>
            <ol>
              <li>
                <p>
                  The procedure page displays the list of experiments which can
                  be accessed by the students(Fig.23)
                </p>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figsa_6}
                alt=""
              />
            </div>
          </section>


          <section style={{ display: "block" }} id="qsa5">
            <div>
              <h2>Add user : Super Admin</h2>
              <ol>
                <li>
                  <p>
                    Super admin can create accounts for Admin/Teacher/Student on
                    Add user page.
                  </p>
                </li>
                <li>
                  <p>
                    Enter the Admin/Teacher/Student name and email address on
                    add user page and select the role.
                  </p>
                </li>
                <li>
                  <p>Finally, click the create user Button (Fig.24 )</p>
                </li>
              </ol>
            </div>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figsa_7}
                alt=""
              />
            </div>
          </section>


          <section style={{ display: "block" }} id="qsa6">
            <h2>Setting page: Super Admin</h2>
            <p>&nbsp;</p>
            <ol>
              <li>
                <p>Click the setting option</p>
              </li>
              <li>
                <p>
                  In the manage user section, Super admin can able to
                  view/edit/update the list of student role/admin role/teacher
                  role/country/ year/semester/access lab.
                </p>
              </li>
              <li>
                <p>
                  Enter the search option in the top right corner, now you can
                  search: Name\Email\Role\Id\Country\college name.
                </p>
              </li>
              <li>
                <p>
                  Now choose the selective Admin/ teacher/student column and if
                  any changes occur on that account you can able to update and
                  can able to add access lab to that account.
                </p>
              </li>
              <li>
                <p>
                  Super admin can only edit on Role, country, year, state,
                  semester, and list of labs available<strong>(</strong>Fig.25)
                </p>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figsa_8}
                alt=""
              />
            </div>
          </section>


          <section style={{ display: "block" }} id="qsa7">
            <h2>Support page: Super Admin</h2>
            <ol>
              <li>
                <p>Super admin can give their feedback here.</p>
              </li>
              <li>
                <p>
                  Super admin can list the bugs or features in the input tag and
                  specify the feedback category.
                </p>
              </li>
              <li>
                <p>Super admin can upload the image more specifically.</p>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figsa_9}
                alt=""
              />
            </div>
          </section>
        </div>
        {/* /////////////////////////////////// */}
        <section style={{ display: "block" }} id="qa1">
          <h3>PROFILE: Admin Role</h3>
          <ol>
            <li>
              <p>Go to the profile page</p>
            </li>
            <li>
              <p>Click the edit option you can edit your profile page</p>
            </li>
            <li>
              <p>
                Now you can edit your country and state name on the profile
                page(Fig.27).
              </p>
            </li>
          </ol>
          <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figa_1}
                alt=""
              />
            </div>
        </section>

        <section style={{ display: "block" }} id="qa2">
          <h2>My page: Admin Role</h2>
          <ol>
            <li>
              <p>A list of experiments can be shown</p>
            </li>
            <li>
              <p>
                Enter the search option you can search
                <strong>
                  : Id/procedure name/lab name/submitted by/submitted time.{" "}
                </strong>
                (Fig.19)and find the experiment
              </p>
            </li>
            <li>
              <p>
                To open the experiment, the <strong>ADMIN</strong> can see the
                values in the tabular column (Fig.20)
              </p>
            </li>
          </ol>
          <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figa_2}
                alt=""
              />
            </div>
            <br />
            <br />
            <br />
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figa_3}
                alt=""
              />
            </div>
        </section>


        <section style={{ display: "block" }} id="qa3">
          <h2>Runz: Admin role</h2>
          <ol>
            <li>
              <p>
                Click the search option you can search:{" "}
                <strong>
                  Id/ procedure name/lab name/assigned by/description (Fig.21)
                </strong>
              </p>
            </li>
            <li>
              <p>
                Click the &ldquo; <strong>+ &ldquo;</strong>option
              </p>
            </li>
            <li>
              <p>
                now you can enter the <strong>experiment description </strong>
                and select the lab type (Fig 22)
              </p>
            </li>
            <li>
              <p>
                Select the <strong>procedure name</strong> and click the{" "}
                <strong>save</strong> option.
              </p>
            </li>
          </ol>
          <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figa_4}
                alt=""
              />
            </div>
            <br />
            <br />
            <br />
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figa_5}
                alt=""
              />
            </div>
        </section>
        <section style={{ display: "block" }} id="qa4">
          <div>
            <h2>Procedure: Admin role</h2>
          </div>
          <ol>
            <li>
              <p>
                The procedure page displays the list of experiments that can be
                accessed by the Admin(Fig.23)
              </p>
            </li>
          </ol>
          <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figa_6}
                alt=""
              />
            </div>
        </section>
        <section style={{ display: "block" }} id="qa5">
            <h2>Add user: Admin role</h2>
            <ol>
              <li>
                <p>
                  Admin can create accounts for teacher/ students on Add user
                  page
                </p>
              </li>
              <li>
                <p>
                  Enter the <strong>teacher</strong>/ <strong>student</strong>{" "}
                  <strong>name</strong> and <strong>email</strong>{" "}
                  <strong>address</strong> on add user page and select the role.
                </p>
              </li>
              <li>
                <p>Finally, click the create user Button(Fig.24 )</p>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figa_7}
                alt=""
              />
            </div>
        </section>
        <section style={{ display: "block" }} id="qa6">
          <h2>Setting page: Admin role</h2>
          <p>&nbsp;</p>
          <ol>
            <li>
              <p>Click the setting option</p>
            </li>
            <li>
              <p>
                In the manages user section, Admin can able to view/edit/update
                the list of students/teacher role/country/ year/semester/access
                lab.
              </p>
            </li>
            <li>
              <p>
                Enter the search option in the top right corner, now you can
                search: Name\Email\Role\Id\Country\college name.
              </p>
            </li>
            <li>
              <p>
                Now choose the selective teacher/student column and if any
                changes occur on that account you can able to update and can
                able to add access lab to that account.
              </p>
            </li>
            <li>
              <p>
                Admin can only edit on
                <strong>
                  Role, country, year, state, semester, and list of labs
                  available (
                </strong>
                Fig.25)
              </p>
            </li>
          </ol>
          <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figa_8}
                alt=""
              />
            </div>
        </section>
        <section style={{ display: "block" }} id="qa7">
            <h2>Support page: Admin role</h2>
            <ol>
              <li>
                <p>Admin can give their feedback here.</p>
              </li>
              <li>
                <p>
                  Admin can list the bugs or features in the input tag and
                  specify the feedback category(Fig 26)
                </p>
              </li>
              <li>
                <p>Admin can upload the image more specifically.</p>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figa_9}
                alt=""
              />
            </div>
        </section>
        <section style={{ display: "block" }} id="qa8">
            <h2>LOGOUT :</h2>
            <p>You can log out of the system as follows</p>
            <ol>
              <li>
                <p>Click on the user name icon in the top right corner.</p>
              </li>
              <li>
                <p>Click on the &lsquo;'LOGOUT&rsquo;'option(Fig.10)</p>
              </li>
            </ol>
            <div>
              <img
                style={{ width: "600px", height: "400px",  display: "block", marginLeft: "auto",  marginRight: "auto", width: "50%", }}
                src={figlo}
                alt=""
              />
            </div>
        </section>
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
           <ListItemButton onClick={()=>{setOpenstudent(!openstudent)}}>
      
        <ListItemText primary="Student" />
        {openstudent ? <ExpandLess /> : <ExpandMore />}
      </ListItemButton>


      <Collapse in={openstudent} timeout="auto" unmountOnExit>
        <List component="div" disablePadding>
        <Link
            activeClass="active"
            to="q1"
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
            to="q2"
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
            to="q3"
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
            to="q4"
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
            to="q5"
            spy={true}
            smooth={true}
            duration={500}
            offset={-100}
          >
            <MenuItem>
              <ListItemText>Procedure</ListItemText>
            </MenuItem>
          </Link>
          <Link
            activeClass="active"
            to="q6"
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
            to="q7"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>Support</ListItemText>
            </MenuItem>
          </Link>
        </List>
      </Collapse>




          
          <Divider />
          {/* /////////////////////////////////////////////////////////////////// */}
          <ListItemButton onClick={()=>{setOpenteacher(!openteacher)}}>
      
      <ListItemText primary="Teachers" />
      {openteacher ? <ExpandLess /> : <ExpandMore />}
    </ListItemButton>

    <Collapse in={openteacher} timeout="auto" unmountOnExit>
        <List component="div" disablePadding>


          <Link
            activeClass="active"
            to="qt1"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>Edit Profile</ListItemText>
            </MenuItem>
          </Link>
          <Link
            activeClass="active"
            to="qt2"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>My Page</ListItemText>
            </MenuItem>
          </Link>
          <Link
            activeClass="active"
            to="qt3"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>Runz</ListItemText>
            </MenuItem>
          </Link>{" "}
          <Link
            activeClass="active"
            to="qt4"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>Procedure</ListItemText>
            </MenuItem>
          </Link>
          <Link
            activeClass="active"
            to="qt5"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>Add User</ListItemText>
            </MenuItem>
          </Link>
          <Link
            activeClass="active"
            to="qt6"
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
            to="qt7"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>Settings</ListItemText>
            </MenuItem>
          </Link>
          </List>
      </Collapse>

          <Divider/>
          {/* //////////////////////////////////////////////////////////////////////////// */}
          <ListItemButton onClick={()=>{setOpensuperadmin(!opensuperadmin)}}>
      
      <ListItemText primary="Super Admin" />
      {opensuperadmin ? <ExpandLess /> : <ExpandMore />}
    </ListItemButton>
      
    <Collapse in={opensuperadmin} timeout="auto" unmountOnExit>
        <List component="div" disablePadding> 
       
       
          <Link
            activeClass="active"
            to="qsa1"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>Edit Profile</ListItemText>
            </MenuItem>
          </Link><Link
            activeClass="active"
            to="qsa2"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>My Page</ListItemText>
            </MenuItem>
          </Link><Link
            activeClass="active"
            to="qsa3"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>Runz</ListItemText>
            </MenuItem>
          </Link><Link
            activeClass="active"
            to="qsa4"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>Procedure</ListItemText>
            </MenuItem>
          </Link><Link
            activeClass="active"
            to="qsa5"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>Add User</ListItemText>
            </MenuItem>
          </Link><Link
            activeClass="active"
            to="qsa6"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>Settings</ListItemText>
            </MenuItem>
          </Link><Link
            activeClass="active"
            to="qsa7"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>Support</ListItemText>
            </MenuItem>
          </Link>
          </List>
      </Collapse>

      <Divider /> 
        {/* //////////////////////////////////////////////////////////////////// */}
        <ListItemButton onClick={()=>{setOpenadmin(!openadmin)}}>
      
      <ListItemText primary="Admin" />
      {openadmin ? <ExpandLess /> : <ExpandMore />}
    </ListItemButton>
    
    <Collapse in={openadmin} timeout="auto" unmountOnExit>
        <List component="div" disablePadding>
        <Link
            activeClass="active"
            to="qa1"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>Profile</ListItemText>
            </MenuItem>
          </Link>
          <Link
            activeClass="active"
            to="qa2"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>My Page</ListItemText>
            </MenuItem>
          </Link>
          <Link
            activeClass="active"
            to="qa3"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>Runz</ListItemText>
            </MenuItem>
          </Link>
          <Link
            activeClass="active"
            to="qa4"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>Procedure</ListItemText>
            </MenuItem>
          </Link>
          <Link
            activeClass="active"
            to="qa5"
            spy={true}
            smooth={true}
            offset={-100}
            duration={500}
          >
            <MenuItem>
              <ListItemText>Add User</ListItemText>
            </MenuItem>
          </Link>
          <Link
            activeClass="active"
            to="qa6"
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
            to="qa7"
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
            to="qa8"
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
      </Collapse>

        </List>
        </Paper>
        </div>
      </div>
      </Grid>
      
      </Grid>
  );
};

export default Helpguide1;
