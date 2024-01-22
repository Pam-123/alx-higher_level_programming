#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow, *mid_node;
	listint_t *second_half, *temp;
	int is_palindrome = 1;

	slow = fast = *head;
	prev_slow = NULL;

	while (fast != NULL && fast->next != NULL)
	{
	    fast = fast->next->next;

	    temp = slow;
	    slow = slow->next;
	    temp->next = prev_slow;
	    prev_slow = temp;
	}

	if (fast != NULL)
	{
	    mid_node = slow;
	    slow = slow->next;
	}

	second_half = slow;

	while (prev_slow != NULL && second_half != NULL)
	{
	    if (prev_slow->n != second_half->n)
	    {
	        is_palindrome = 0;
	        break;
	    }
	    prev_slow = prev_slow->next;
	    second_half = second_half->next;
	}

	while (mid_node != NULL)
	{
	    temp = prev_slow;
	    prev_slow = prev_slow->next;
	    temp->next = mid_node;
	    mid_node = mid_node->next;
	    temp->next->next = temp;
	}

	return (is_palindrome);
}
