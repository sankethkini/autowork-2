import React, { Component } from 'react';

class App extends Component {
    componentDidMount(){     window.location.href = "http://localhost:8000";  }
  render() {
   
    
    return (
        <div>
       <h2>Autowork</h2>
      </div>
    );
  }
}

export default App;