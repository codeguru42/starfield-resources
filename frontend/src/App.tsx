import {DataGrid, GridColDef} from "@mui/x-data-grid";
import {useEffect, useState} from "react";
import {ApiApiFactory, Star} from "./api";

function App() {
  const [stars, setStars] = useState<Star[]>([])

  useEffect( () => {
    const api = ApiApiFactory();
    api.listStars()
      .then((stars) => {
        setStars(stars.data)
      })
  }, [])

  const columns: GridColDef[] = [
    {
      field: 'name',
      headerName: 'Star',
    },
    {
      field: 'level',
      headerName: 'Level',
    },
  ]

  return (
    <>
      <h1>Starfield Resources</h1>
      <DataGrid columns={columns} rows={stars}/>
    </>
  )
}

export default App
