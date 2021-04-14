export const LEADERBOARD_LOADED = 'LEADERBOARD_LOADED';
export const LOGGED_IN = 'LOGGED_IN';
export const MOVE_OBJECT = 'MOVE_OBJECT';
export const START_GAME = 'START_GAME';

export const leaderboardLoaded = players => ({
    type: LEADERBOARD_LOADED,
    players,
});

export const loggedIn = player => ({
    type: LOGGED_IN,
    player,
});

export const moveObjects = mousePosition => ({
    type: MOVE_OBJECT,
    mousePosition,
});

export const startGame = () => ({
    type: START_GAME,
});