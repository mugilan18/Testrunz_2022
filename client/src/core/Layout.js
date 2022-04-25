import React, { Fragment } from "react";
import { Link, withRouter } from "react-router-dom";

function Layout(props) {
  const isActive = (path) => {
    if (props.match.path === path) {
      return { color: "#000" };
    } else {
      return { color: "#fff" };
    }
  };
  const nav = () => (
    <></>
  );
  return (
    <Fragment>
      {nav()}
      <div className="container">{props.children}</div>
    </Fragment>
  );
}

export default withRouter(Layout);
