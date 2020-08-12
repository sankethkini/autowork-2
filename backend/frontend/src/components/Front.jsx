import React from 'react';
import ReactDom from 'react-dom';
import { Button, Form, FormGroup, Label, Input} from 'reactstrap';
import Maruti from "./Maruti";
import Hyundai from "./Hyundai"

class Front extends React.Component{
  constructor(props){
    super(props);
    this.state={
      make:1
    
    }
    this.myChangeHandler=this.myChangeHandler.bind(this);
    this.mySubmitHandler=this.mySubmitHandler.bind(this);
  }
  myChangeHandler(event){
    let name=event.target.name
    let value=event.target.value
    this.setState({make:value})
  }
  mySubmitHandler(event){
    this.setState({next:this.state.make})
    if(this.state.make === 1){
      ReactDom.render(
        <Maruti />,document.getElementById('root')
      );
      
    }
    else{
      ReactDom.render(
        <Hyundai/>,document.getElementById('root')
      );
    }
  }
  render(){
    
  return (
   <div className="container">
   <div className="jumbotron">
     <h1>
       Welcome to Autowork
     </h1>
    </div>
     <br></br>
    <br></br>
    <p>
      This website will help you in predicting the right resell price for your car.<br></br>
      This will use machine learning for prediction and interpret it for you.<br></br>
      Just you have to give some details acout your car such as make,model,new price etc.
      The interpretation basically tells you how each feature is affecting your output<br></br>
    </p>
    <br></br>
    <Form onSubmit={this.mySubmitHandler}>
        <FormGroup>
          <Label for="Email">Enter your Email:</Label>
          <Input id="Email" type="email" required>
          </Input>
        </FormGroup>
        <FormGroup>
          <Label for="make"></Label>
          <Input id="make" type="select" name="make" value={this.state.make} onChange={this.myChangeHandler}>
            <option value="1">Maruti</option>
            <option value="2">Hyundai</option>
          </Input>
          </FormGroup>
          <br></br>
          <br></br>
          <FormGroup>
                <Button type="submit" color="success" disabled={false}>Submit</Button>
          </FormGroup>
    </Form>

    </div>
  );
  }
}


export default Front;
