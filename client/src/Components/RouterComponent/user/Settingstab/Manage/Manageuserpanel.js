import React from 'react'
import { useStateValue } from '../../../../../data/StateProvider';

import Manageusertable from './Manageusertable';

const Manageuserpanel = () => {
    const [{ user }, dispatch] = useStateValue();
  return (
    <div>
    
        <Manageusertable/>
     

    </div>
  )
}

export default Manageuserpanel