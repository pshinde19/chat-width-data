import { useState } from 'react'
import { router } from './routes/approutes'
import './App.css'
import { RouterProvider } from 'react-router-dom'


function App() {
  return (

    <RouterProvider router={router} />
  )
}

export default App
