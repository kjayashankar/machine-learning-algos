function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %

	siz = size(theta);
	thetaTemp = theta;
	for thetaItr = 1:siz
		thetaTemp(thetaItr) = theta(thetaItr) - alpha * (1/m) *(X*theta - y)'*X(:,thetaItr);
		
	
	
	end
	theta = thetaTemp;




    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCost(X, y, theta);
	if iter > 1
		if (J_history(iter) > J_history(iter-1))
			%disp('found the ascent, breaking out %d')
			%disp(iter)
			break
		endif
	endif


end

end
