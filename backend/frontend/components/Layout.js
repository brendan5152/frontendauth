import React from "react"
import Nav from "./Nav"

const Layout = ({ children }) => {
  return (
    <>
    <Nav />
    <div className="h-full w-full mx-auto max-w-7xl ">
    
    {children}
    </div>
    </>
  );

}

export default Layout;