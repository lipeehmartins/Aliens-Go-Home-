import React from 'react';
import PropTypes from 'prop-types';
import styled, { keyframes } from 'styled-components';
import FlyingObjectTop from './FlyingObjectTop';
import FlyingObjectBase from './FlyingObjectBase';
import { gameHeight } from '../utils/constants';

const moveVertically = keyframes
`
0% {
    transform: translateY(y)
}

100% {
    transform: translateY(${gameHeight}px);
}
`;

const Move = styled.g
`
animation: ${moveVertically} 4s linear;
`

const FlyingObject = props => (
    <Move>
        <FlyingObjectBase position={props.position} />
        <FlyingObjectTop position={props.position} />
    </Move>
);

FlyingObjectTop.propTypes = {
    position: PropTypes.shape({
        x: PropTypes.number.isRequired,
        y: PropTypes.number.isRequired
    }).isRequired,
};

export default FlyingObject;