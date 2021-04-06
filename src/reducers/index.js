import { MOVE_OBJECT } from '../actions';
import moveObjects from './moveObjects';

const initialState = {
    angle: 45,
  };
  
  function reducer(state = initialState, action) {
    switch (action.type) {
      case MOVE_OBJECT:
        return moveObjects(state, action);
    default:
      return state;
    }
  }
  
  export default reducer;