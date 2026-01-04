import {createBrowserRouter} from "react-router-dom"
import Applayout from '../components/Applayout/Applayout'
import ErrorPage from '../components/Errorpage/Errorpage'


export const router=createBrowserRouter([
  {

    Component:Applayout,
    errorElement:<ErrorPage/>,
    children: [
      {
        path: "/",
        index: true,
        element:"<div>hello</div>",
        errorElement:<ErrorPage/>,
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
    element:<ErrorPage/>
  },
])
