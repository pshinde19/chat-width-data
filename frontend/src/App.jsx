import { useState } from 'react'
import {createBrowserRouter, RouterProvider} from "react-router-dom"
import './App.css'
import Applayout from './components/Applayout/Applayout'
import ErrorPage from './components/Errorpage/Errorpage'


const router=createBrowserRouter([
  {

    Component:Applayout,
    errorElement:ErrorPage,
    children: [
      {
        path: "/",
        index: true,
        element:"<div>hello</div>",
        errorElement:ErrorPage,
      }
    ]
  },
  {
    path: "/admin",
    index: true,
    element:"<div>admin</div>",
  },
  {
    path: "/access",
    index: true,
    element:"<div>access</div>",
  },
  {
    path: "/error",
    index: true,
    Component:ErrorPage
  },
])


function App() {
  return (

    <RouterProvider router={router} />
  )
}

export default App
