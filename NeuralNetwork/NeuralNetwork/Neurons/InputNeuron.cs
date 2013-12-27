﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NeuralNetwork.Neurons
{
    /// <summary>
    /// Type specific implementation of the neuron class for input neurons.
    /// </summary>
    public class InputNeuron : Neuron
    {
        /// <summary>
        /// Returns the inactivated net value.
        /// </summary>
        /// <returns></returns>
        public override double GetOutput(Sigmoid activation)
        {
            return Net;
        }
    }
}
