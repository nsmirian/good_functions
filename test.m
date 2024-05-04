classdef MyAPP < matlab.apps.AppBase

    properties (Access = private)
        Future1 % Future object for function1
        Future2 % Future object for function2
    end

    methods (Access = private)

        % Button pushed function: Button1
        function Button1Pushed(app, event)
            % Start function1 in a separate worker
            app.Future1 = parfeval(@function1, 0); % Use 0 workers for automatic assignment
        end

        % Button pushed function: Button2
        function Button2Pushed(app, event)
            % Start function2 in a separate worker
            app.Future2 = parfeval(@function2, 0); % Use 0 workers for automatic assignment
        end

        % Function to print 1 repeatedly
        function function1()
            while true
                disp(1);
                pause(1); % Adjust the pause time as needed
            end
        end

        % Function to print 2 repeatedly
        function function2()
            while true
                disp(2);
                pause(1); % Adjust the pause time as needed
            end
        end

    end

    % App initialization and construction
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Create UIFigure
            app.UIFigure = uifigure;

            % Create Button1
            app.Button1 = uibutton(app.UIFigure, 'push');
            app.Button1.Position = [100 100 100 22];
            app.Button1.Text = 'Button 1';
            app.Button1.ButtonPushedFcn = createCallbackFcn(app, @Button1Pushed, true);

            % Create Button2
            app.Button2 = uibutton(app.UIFigure, 'push');
            app.Button2.Position = [100 50 100 22];
            app.Button2.Text = 'Button 2';
            app.Button2.ButtonPushedFcn = createCallbackFcn(app, @Button2Pushed, true);

            % Show the UIFigure
            app.UIFigure.Visible = 'on';
        end
    end
end
