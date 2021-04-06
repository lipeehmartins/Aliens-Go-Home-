export const MOVE_OBJECT = 'MOVE_OBJECT';

export const moveObjects = mousePosition => ({
    type: MOVE_OBJECT,
    mousePosition,
});