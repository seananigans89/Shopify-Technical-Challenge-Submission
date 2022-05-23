import './App.css';
import React, { useEffect, useState } from 'react';
import {Formik, Form, Field} from 'formik'

function App() {
  const [inventory, setInventory] = useState([])
  


  const items = [1, 2, 3, 4, 5]
  const listItems = items.map((item, key) => 
  <li key={key}>{item}</li> 
  )

  const fetchItems = async() =>{
    await fetch('http://127.0.0.1:8000/items/', {
      method: 'GET',
    }).then(res => res.json()
    ).then(data => setInventory(data))
  }
  useEffect(() => {
    fetchItems()
  }, []);

  const createItem = async (itemValues)  => {
    console.log(itemValues)
    await fetch('http://127.0.0.1:8000/items/', {
      method: 'POST',
      body: itemValues,
      headers:{
      'Accept': 'application/json, text/plain, */*',
      'Content-Type': 'application/json',
      }
  
    })
    .then(res => res.json()
    ).then(data => setInventory(...inventory, data))
  
  }

  return (
    <div className="App">
      <h1>Inventory Manager</h1>
      <Formik
      initialValues={{
        name: '',
        quantity: '',
        weight: '',
      
      }}
      onSubmit={async (values) => {
        createItem(JSON.stringify(values));
      }}
    >
      <Form>
        <label htmlFor="name">Item Name</label>
        <Field id="name" name="name" placeholder="" />

        <label htmlFor="quantity">Quantity</label>
        <Field id="quantity" name="quantity" placeholder="" type="number"/>

        <label htmlFor="weight">Weight</label>
        <Field
          id="weight"
          name="weight"
          placeholder=""
          type="number"
        />
        <button type="submit">Create Item</button>
      </Form>
    </Formik>
    <div>
      <ul>
        {listItems}
      </ul>
    </div>
    </div>
  );
}

export default App;
