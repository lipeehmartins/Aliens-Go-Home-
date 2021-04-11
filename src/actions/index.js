export const MOVE_OBJECT = 'MOVE_OBJECT';
export const START_GAME = 'START_GAME';

export const moveObjects = mousePosition => ({
    type: MOVE_OBJECT,
    mousePosition,
});

export const startGame = () => ({
    type: START_GAME,
});