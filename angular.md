# AngularJS

## NG-pilosophy
* declarative vs imperative

## An Overview
* module
* view
	* connected by the $scope
* controller
* service between the controller
* directive -> view

## Module
* HTML
```html
<div ng-app="tekflix">
	<input type="text" ng-model="sg"/>
	<br><br>
	{{ msg }}
</dv>
```
```js
```

## Directive
* changes the dashes to camelcase
```html
<div ng-app="tekflix">
	<tek-movie src="http://jdksafjldf"></tek-movie>
```
```js
```
* creating a module
```html
<div ng-app="tekFlix">
	<tek-movie-spinner></tek-movie-spinner>
</div>
```
```js
angular.module('tekFlix')
```

## Directive - Test
* $scope and $digest

## Service
* provider, factory, service: functions off of module, all very connected
* just stick with service, if just starting out

## Service - Test
* test in isolation, run fast and not have external dependencies
* Angular provides mock services

## Filter
* there are built-in ones

## E2E Testing
* protractor - find elements & setup scenario

## Angular 2.X
* TypeScript || Dart || JS
* controllers and scopes are going away
* 2-way databinding is kind of going away
* new part: component (like directive)
