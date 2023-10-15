import {DataGrid, GridColDef} from "@mui/x-data-grid";
import {planets} from "./data.ts";

function App() {
  const columns: GridColDef[] = [
    {
      field: 'name',
      headerName: 'Planet',
      width: 150,
    },
    {
      field: 'star',
      headerName: 'Star',
      width: 150,
    }
  ]

  return (
    <>
      <h1>Starfield Resources</h1>
      <DataGrid columns={columns} rows={planets}/>
    </>
  )
}

export default App
