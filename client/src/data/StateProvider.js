import React, { createContext,useContext, useReducer } from "react"

// creating the context layer or preparing the context layer
export const StateContext = createContext();

// wrapping the provider to the whole component as the children
export const StateProvider = ({reducer, initialState, children}) => (
    <StateContext.Provider value={useReducer(reducer, initialState)}>
        {children}
    </StateContext.Provider>
)

// can pull the information from this data layer using this
export const useStateValue = () => useContext(StateContext);

 



