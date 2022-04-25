export const initialState = {
    user: null,
    prosid: null
};

export const actionTypes = {
    SET_USER: "SET_USER",
    SET_PROSID: "SET_PROSID",
};

const reducer = (state, action) =>{
    console.log(action);
    switch(action.type){
        case actionTypes.SET_USER:
            return {
                ...state,
                user: action.user,
            };
        case actionTypes.SET_PROSID:
            return {
                ...state,
                prosid: action.prosid,
            };
        
        default:
            return state;
    }
}

export default reducer;