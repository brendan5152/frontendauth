import React from "react"
import Nav from "./Nav"

const Layout = ({ children }) => {
  return (
    <>
    <Nav />
    <div className="container w-full mx-auto max-w-7xl ">
    
    {children}
    </div>
    </>
  );

}

export default Layout;